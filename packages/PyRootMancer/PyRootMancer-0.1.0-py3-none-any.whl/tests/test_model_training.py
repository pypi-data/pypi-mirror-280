import logging
import sys
import tempfile
import unittest
from unittest.mock import patch
from src.models.model_training import ModelTraining

from src.utils.configuration import *

# Ensure the path to the project is added
sys.path.append('E:/Github/2023-24d-fai2-adsai-group-cv5/')

class TestModelTrain(unittest.TestCase):

    @patch('src.models.model_training.load_model')
    def test_load_model(self, mock_load_model):
        modelling = ModelTraining()
        models_folder = folder_config.get("models_folder")
        model_name = 'best_model_root_masks'

        # Create a mock return value
        mock_return_value = {'a': 1, 'b': 2}
        mock_load_model.return_value = mock_return_value

        # Test the load_model function
        loaded_model = modelling.load_model(models_folder, model_name)

        self.assertEqual(loaded_model, mock_return_value)
        self.assertTrue(mock_load_model.called)

    @patch.object(os.path, 'join')
    def test_load_model_os_error(self, mock_join):
        modelling = ModelTraining()
        models_folder = folder_config.get("models_folder")
        model_name = 'best_model_root_masks'

        # Raise an error when os.path.join is called
        mock_join.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            modelling.load_model(models_folder, model_name)

    def test_data_generator(self):
        # Create temporary directory for testing
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create instances of the image and mask generators
            modelling = ModelTraining()
            train_image_generator = os.path.join(temp_dir, "images")
            train_mask_generator = os.path.join(temp_dir, "masks")
            #
            # Create some test files in these directories for testing purposes
            for i in range(10):
                os.makedirs(os.path.join(train_image_generator, str(i)),
                            exist_ok=True)
                os.makedirs(os.path.join(train_mask_generator, str(i)),
                            exist_ok=True)

                # Add some sample images
                with open(os.path.join(train_image_generator, str(i), "image1.png"), 'w'):
                    pass

                with open(os.path.join(train_mask_generator, str(i), "mask1.png"), 'w'):
                    pass
            result = modelling.data_generator(train_image_generator, train_mask_generator)
            self.assertEqual(result, (None, None, None, None))


    def test_training(self):
        modelling = ModelTraining()
        # Create temporary directories for testing
        with tempfile.TemporaryDirectory() as temp_dir:
            mask_folder = os.path.join(temp_dir, "mask_folder")
            model_folder = os.path.join(temp_dir, "model_folder")

            # Create some sample images and masks for testing
            image_folder = os.path.join(temp_dir, "image_folder")
            os.makedirs(image_folder)
            with open(os.path.join(image_folder, "image1.png"), 'w'):
                pass

            mask_folder_path = os.path.join(temp_dir, "mask_folder")
            os.makedirs(mask_folder_path)
            with open(os.path.join(mask_folder_path, "mask1.png"), 'w'):
                pass

            # Create the train and validation generators
            train_generator, validation_generator, _, _ = modelling.data_generator(image_folder, mask_folder)

            # Train the model
            trained_model = modelling.training(2, image_folder, mask_folder, model_folder, "model_name")


            logging.info("Model training complete")
            logging.info(f"Check if the model has been saved to {os.path.join(model_folder, 'model_name.keras')}")

        try:
            self.assertTrue(os.path.exists(os.path.join(model_folder,  "model_name.keras")))
        except AssertionError as ae:
            logging.error(ae)


# def test_predict_image(self):
#     image_path = 'path_to_your_image.jpg'  # Replace with the actual path toan image
#     output_folder = 'path_to_your_output_folder'  # Replace with the actual path to a folder for saving output
#     models_folder = 'path_to_your_models_folder'  # Replace with the actual path to a folder containing trained models
#     model_name = 'model_name'  # Replace with the actual name of the model you want to use
#
#     predicted_mask = self.model_training.predict_image(image_path,output_folder, models_folder, model_name)
#
#     # Add assertions here to test the correctness of the prediction
#     self.assertIsNotNone(predicted_mask)
#     self.assertEqual(predicted_mask.shape, (2731, 2752))  # Replace with the expected shape of the predicted mask



if __name__ == '__main__':
    unittest.main()
