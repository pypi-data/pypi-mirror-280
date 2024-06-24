import cv2
import pandas as pd
from skan import Skeleton, summarize
import numpy as np
from skimage.transform import resize

from patchify import patchify, unpatchify
from src.features.instance_segmentation import InstanceSegmentation
from src.models.model_training import ModelTraining
from src.features.root_coord_extraction import LandmarkExtraction
from src.utils.configuration import *


class cv_pipeline:
    def __init__(self):
        self.modelling = ModelTraining()
        self.segmentation = InstanceSegmentation()
        self.landmarks = LandmarkExtraction()

    def main(self, image_path):
        pred = self.modelling.predict_image(
            image_path, ".temp", folder_config.get("models_folder"), "best_model_root_masks"
        )
        reverted = self.revert(pred)
        sorted_image_coord_dst_0, sorted_image_coord_dst_1 = self.get_bottom_coordinates(reverted)
        df = self.create_and_sort_dataframe(sorted_image_coord_dst_0, sorted_image_coord_dst_1)
        for i in range(len(df)):
            print(self.get_image_coordinates(df, i))
        return df

    def revert(self, predicted_mask):
        original_image = np.zeros((3006, 4202), dtype=np.uint8)
        im = predicted_mask[0:2816, 0:2816]
        roi_1 = original_image[50 : 2816 + 50, 720 : 2816 + 720]
        overlay_image = (resize(im, roi_1.shape, mode='reflect', anti_aliasing=True) * 255).astype(np.uint8)
        modified_cropped = np.zeros_like(original_image)
        roi = modified_cropped[50 : 2816 + 50, 720 : 2816 + 720]
        result = cv2.addWeighted(roi, 1, overlay_image, 0.7, 0)
        modified_cropped[50 : 2816 + 50, 720 : 2816 + 720] = result
        norm = cv2.normalize(modified_cropped, None, 0, 255, cv2.NORM_MINMAX)
        return norm

    def get_bottom_coordinates(self, input_mask, threshold: int = 50):

        try:
            mask = self.landmarks.opening_closing(self.landmarks.remove_small_components(input_mask))
            df = summarize(Skeleton(mask))
            filtered_df = df[
                (df['image-coord-dst-0'] < 2415) & (df['branch-type'] != 0) & (df['euclidean-distance'] > 20)
            ]

            image_coord_dst_0, image_coord_dst_1 = (
                filtered_df.sort_values(by='image-coord-dst-0', ascending=False)
                .groupby('skeleton-id', as_index=False)
                .agg({'image-coord-dst-0': 'max', 'image-coord-dst-1': 'first'})[
                    ['image-coord-dst-0', 'image-coord-dst-1']
                ]
                .values.T.tolist()
            )

            paired_coords = list(zip(image_coord_dst_0, image_coord_dst_1))
            paired_coords.sort(key=lambda pair: pair[0], reverse=True)
            sorted_image_coord_dst_0, sorted_image_coord_dst_1 = zip(*paired_coords)

            sorted_image_coord_dst_0 = list(sorted_image_coord_dst_0)
            sorted_image_coord_dst_1 = list(sorted_image_coord_dst_1)

            indices_to_remove = set()
            for i in range(len(sorted_image_coord_dst_1)):
                for j in range(i + 1, len(sorted_image_coord_dst_1)):
                    if abs(sorted_image_coord_dst_1[i] - sorted_image_coord_dst_1[j]) <= threshold:
                        if sorted_image_coord_dst_0[i] < sorted_image_coord_dst_0[j]:
                            indices_to_remove.add(i)
                        else:
                            indices_to_remove.add(j)

            filtered_image_coord_dst_0 = [
                val for idx, val in enumerate(sorted_image_coord_dst_0) if idx not in indices_to_remove
            ]
            filtered_image_coord_dst_1 = [
                val for idx, val in enumerate(sorted_image_coord_dst_1) if idx not in indices_to_remove
            ]

            paired_coords = list(zip(filtered_image_coord_dst_0[:5], filtered_image_coord_dst_1[:5]))
            paired_coords.sort(key=lambda pair: pair[1])
            sorted_image_coord_dst_0, sorted_image_coord_dst_1 = zip(*paired_coords)

            return sorted_image_coord_dst_0, sorted_image_coord_dst_1

        except Exception as e:
            print(f"An error occurred: {e}")
            return [], []

    def get_image_coordinates(self, df, num):
        plate = np.array([0.10775, 0.088, 0.057])
        scaling_factors = np.array([1099, 1099]) / np.array([2752, 2731])

        landmark_scaled = df.loc[num, ['X', 'Y']].values * scaling_factors
        print(f'Scaled coordinates of root tip {landmark_scaled}')

        conversion_factors = np.array([150 / 1099, 151 / 1099])
        root_tip_mm = (landmark_scaled * conversion_factors) / np.array([1100, 1091])
        root_tip_position = np.append(root_tip_mm[::-1], 0)

        root_tip_robot_position = plate + root_tip_position
        return root_tip_robot_position

    def create_and_sort_dataframe(self, image_coord_dst_0, image_coord_dst_1):
        df = pd.DataFrame({'X': image_coord_dst_1, 'Y': image_coord_dst_0, 'Z': [0] * len(image_coord_dst_0)})
        sort_x = df.nlargest(5, 'Y').sort_values(by=['Y', 'X'], ascending=[False, True])
        print(f'{len(sort_x)} root tips coordinates found')
        print(sort_x)
        return sort_x


if __name__ == "__main__":
    cv = cv_pipeline()
    cv.main(
        os.path.join(
            folder_config.get("test_folder"),
            "031_43-6-ROOT1-2023-08-08_control_pH7_-Fe+B_f6h1_02-Fish Eye Corrected.png",
        )
    )
