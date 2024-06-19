import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import pandas as pd
from src.features.root_length import RootLengthCalculator


class TestRootLengthCalculator(unittest.TestCase):

    @patch('src.features.root_length.tf.keras.models.load_model')
    def setUp(self, mock_load_model):
        # Mocking the loaded model
        self.mock_model = MagicMock()
        mock_load_model.return_value = self.mock_model

        # Initializing the calculator with a mock model and directory
        self.calculator = RootLengthCalculator(
            img_dir='../task_8_files/Kaggle Dataset/cropped/',
            model_path='../best_models/best_model_root.h5',
            custom_objects={'f1': lambda x: x, 'iou': lambda x: x}
        )

    def test_predict_image(self):
        # Create a dummy image
        img = np.random.randint(0, 256, (500, 500, 3), dtype=np.uint8)

        # Mock the model's predict method
        self.mock_model.predict.return_value = [np.random.rand(256, 256, 1)]

        predicted_mask = self.calculator.predict_image(img, 256)

        # Check if the predicted mask has the correct shape
        self.assertEqual(predicted_mask.shape, (500, 500))

    @patch('src.features.root_length.os.listdir')
    @patch('src.features.root_length.cv2.imread')
    def test_process_images(self, mock_imread, mock_listdir):
        # Mock the list of files in the directory
        mock_listdir.return_value = ['test_image.tif']

        # Mock the image reading
        mock_imread.return_value = np.random.randint(0, 256, (500, 500, 3), dtype=np.uint8)

        # Mock the predict_image method
        with patch.object(self.calculator, 'predict_image', return_value=np.random.rand(500, 500)) as mock_predict:
            self.calculator.process_images()

            # Check if the predict_image method was called
            mock_predict.assert_called()

            # Check if results were appended
            self.assertGreater(len(self.calculator.results), 0)

    def test_calculate_length(self):
        # Create a dummy skeleton and summary
        skeleton = np.zeros((100, 100), dtype=np.uint8)
        skeleton[50, :] = 1  # A horizontal line

        summary = pd.DataFrame({
            'node-id-src': [0, 1],
            'node-id-dst': [1, 2],
            'euclidean-distance': [50, 50],
            'image-coord-src-0': [50, 50],
            'image-coord-src-1': [0, 50],
            'image-coord-dst-0': [50, 50],
            'image-coord-dst-1': [50, 100]
        })

        length = self.calculator.calculate_length(skeleton, summary)

        # The length should be 100 for a horizontal line spanning the image
        self.assertEqual(length, 100)

    @patch('src.features.root_length.os.path.exists')
    @patch('src.features.root_length.pd.DataFrame.to_csv')
    def test_save_results(self, mock_to_csv, mock_exists):
        # Mock the existence check to always return False (file doesn't exist)
        mock_exists.return_value = False

        # Create some dummy results
        self.calculator.results = [
            {'Plant ID': 'test_plant_1', 'Length (px)': 100},
            {'Plant ID': 'test_plant_2', 'Length (px)': 150}
        ]

        # Save results
        self.calculator.save_results('dummy_path.csv')

        # Check if to_csv was called
        mock_to_csv.assert_called_once()

if __name__ == '__main__':
    unittest.main()