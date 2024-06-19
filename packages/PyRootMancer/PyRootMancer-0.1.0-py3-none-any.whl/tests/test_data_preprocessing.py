import unittest
from unittest.mock import patch, MagicMock, call
import cv2
import numpy as np

from src.utils.configuration import *
from src.data.data_preprocessing import DataPipelineSetup

class TestDataPipelineSetup(unittest.TestCase):

    #### CREATING FOLDER TEST ######
    @patch('src.data.data_preprocessing.os.makedirs')
    @patch('src.data.data_preprocessing.get_project_root', return_value="/path/to/base/folder")
    def test_create_folders(self, mock_get_project_root, mock_makedirs):
        processor = DataPipelineSetup()

        processor.create_folders()
        expected_calls = [call(folder, exist_ok=True) for folder in folder_config.values()]
        mock_makedirs.assert_has_calls(expected_calls, any_order=True)


    ###### UNZIPPING FUNCTION TEST ######
    @patch('src.data.data_preprocessing.os.scandir')
    @patch('src.data.data_preprocessing.ZipFile')
    @patch('src.data.data_preprocessing.logging.warning')
    @patch('src.data.data_preprocessing.logging.info')
    def test_unzip_existing_files(self, mock_info, mock_warning, mock_zipfile, mock_scandir):
        processor = DataPipelineSetup()

        mock_scandir.return_value = [MagicMock(is_file=MagicMock(return_value=True))]
        processor.unzip(keyword="train")
        mock_warning.assert_called_once_with('Files already exist in images. Aborting unzip operation to prevent overwriting.')
        mock_zipfile.assert_not_called()
        mock_info.assert_not_called()


    @patch('src.data.data_preprocessing.os.rename')
    @patch('src.data.data_preprocessing.shutil.rmtree')
    @patch('src.data.data_preprocessing.os.scandir', return_value=[])
    @patch('src.data.data_preprocessing.os.walk', return_value=[('root', [], ['file1.jpg', 'file2.jpg'])])
    @patch('src.data.data_preprocessing.ZipFile')
    @patch('src.data.data_preprocessing.logging.info')
    def test_unzip_train(self, mock_info, mock_zipfile, mock_walk, mock_scandir, mock_rmtree, mock_rename):
        processor = DataPipelineSetup()

        with patch('src.data.data_preprocessing.os.makedirs'):
            processor.unzip(keyword="train")
            mock_zipfile.assert_called_once_with(os.path.join(folder_config.get("raw_data_folder"), "train.zip"), 'r')
            mock_zipfile_instance = mock_zipfile.return_value.__enter__.return_value
            mock_zipfile_instance.extractall.assert_called_once_with("train")
            expected_info_calls = [
                call('train file unzipping...'),
                call('2 png images in train zip folder'),
                call('Done!')
            ]
            mock_info.assert_has_calls(expected_info_calls)

    @patch('src.data.data_preprocessing.os.rename')
    @patch('src.data.data_preprocessing.shutil.rmtree')
    @patch('src.data.data_preprocessing.os.scandir', return_value=[])
    @patch('src.data.data_preprocessing.os.walk', return_value=[('root', [], ['file1.jpg', 'file2.jpg'])])
    @patch('src.data.data_preprocessing.ZipFile')
    @patch('src.data.data_preprocessing.logging.info')
    def test_unzip_test(self, mock_info, mock_zipfile, mock_walk, mock_scandir, mock_rmtree, mock_rename):
        processor = DataPipelineSetup()

        with patch('src.data.data_preprocessing.os.makedirs'):
            processor.unzip(keyword="train")
            mock_zipfile.assert_called_once_with(os.path.join(folder_config.get("raw_data_folder"), "train.zip"), 'r')
            mock_zipfile_instance = mock_zipfile.return_value.__enter__.return_value
            mock_zipfile_instance.extractall.assert_called_once_with("train")
            expected_info_calls = [
                call('train file unzipping...'),
                call('2 png images in train zip folder'),
                call('Done!')
            ]
            mock_info.assert_has_calls(expected_info_calls)

    @patch('src.data.data_preprocessing.os.rename')
    @patch('src.data.data_preprocessing.shutil.rmtree')
    @patch('src.data.data_preprocessing.os.scandir', return_value=[])
    @patch('src.data.data_preprocessing.os.walk', return_value=[('root', [], ['root_mask1.tiff', 'shoot_mask1.tif'])])
    @patch('src.data.data_preprocessing.ZipFile')
    @patch('src.data.data_preprocessing.logging.info')
    def test_unzip_masks(self, mock_info, mock_zipfile, mock_walk, mock_scandir, mock_rmtree, mock_rename):
        processor = DataPipelineSetup()

        with patch('src.data.data_preprocessing.os.makedirs'):
            processor.unzip(keyword="masks")
            mock_zipfile.assert_called_once_with(os.path.join(folder_config.get("raw_data_folder"), "masks.zip"), 'r')
            mock_zipfile_instance = mock_zipfile.return_value.__enter__.return_value
            mock_zipfile_instance.extractall.assert_called_once_with("masks")
            expected_info_calls = [
                call('masks file unzipping...'),
                call('1 tiff images class root in masks zip folder'),
                call('1 tiff images class shoot in masks zip folder'),
                call('Done!')
            ]
            mock_info.assert_has_calls(expected_info_calls)


    
    #### CROPPING FUNCTION TEST #####
    @patch('src.data.data_preprocessing.os.listdir')
    @patch('src.data.data_preprocessing.cv2.imread')
    @patch('src.data.data_preprocessing.cv2.imwrite')
    @patch('src.data.data_preprocessing.tq.tqdm')
    @patch('src.data.data_preprocessing.logging.error')
    @patch('src.data.data_preprocessing.logging.info')
    def test_crop(self, mock_info, mock_error, mock_tqdm, mock_imwrite, mock_imread, mock_listdir):
        processor = DataPipelineSetup()
        folder = folder_config.get("test_folder")

        # Set up mock return values and side effects
        test_image_1 = '030_43-2-ROOT1-2023-08-08_pvdCherry_OD001_Col0_05-Fish Eye Corrected.png'
        test_image_2 = '030_43-19-ROOT1-2023-08-08_pvdCherry_OD001_Col0_04-Fish Eye Corrected.png'

        mock_listdir.return_value = [test_image_1, test_image_2]
        mock_imread.side_effect = [
            MagicMock(shape=(3000, 3000, 3)),  # for image1.png
            MagicMock(shape=(3000, 3000)),    # for image2.tif
        ]
        mock_tqdm.return_value = enumerate(mock_listdir.return_value)

        # Call the crop method
        processor.crop(folder)

        # Assert listdir was called with the correct folder
        mock_listdir.assert_called_once_with(folder)

        # Assert imread was called with the correct file paths
        expected_image_1_path = os.path.join(folder, test_image_1)
        expected_image_2_path = os.path.join(folder, test_image_2)

        # Check the actual calls to imread
        actual_calls = [args[0] for args, _ in mock_imread.call_args_list]
        print("Actual imread calls:", actual_calls)

        self.assertIn(expected_image_1_path, actual_calls)
        self.assertIn(expected_image_2_path, actual_calls)

        # Assert imwrite was called with the correct file paths and processed images
        # normalized_image = mock_imread.side_effect[0][75:2800, 750:2300]
        # mask_image = mock_imread.side_effect[1][75:2800, 750:2300]

        # mock_imwrite.assert_any_call(expected_image_1_path, )
        # mock_imwrite.assert_any_call(expected_image_2_path, )

        # # Assert the progress bar was initialized correctly
        # mock_tqdm.assert_called_once_with(enumerate(mock_listdir.return_value), total=2, bar_format='{l_bar}%s{bar}%s{r_bar}' % ('\033[38;2;70;130;180m', '\033[0m'))
        #
        # # Assert logging info was called to indicate completion
        # mock_info.assert_called_once_with(f'Cropping completed successfully from {os.path.basename(folder)}')

        # Ensure no errors were logged
        # mock_error.assert_not_called()



    ##### PADDER FUNCTION TEST #####
    @patch('src.data.data_preprocessing.cv2.copyMakeBorder')
    def test_padder(self, mock_copyMakeBorder):
        processor = DataPipelineSetup()
        patch_size = param_config.get("patch_size")
        # Create a test image with dimensions that are not divisible by patch_size
        test_image = np.random.randint(0, 256, (1000, 750, 3), dtype=np.uint8)

        # Expected padding calculations
        h, w = test_image.shape[:2]
        height_padding = ((h // patch_size) + 1) * patch_size - h
        width_padding = ((w // patch_size) + 1) * patch_size - w

        top_padding = height_padding // 2
        bottom_padding = height_padding - top_padding
        left_padding = width_padding // 2
        right_padding = width_padding - left_padding

        # Create the expected padded image using cv2.copyMakeBorder
        expected_padded_image = cv2.copyMakeBorder(
            test_image, top_padding, bottom_padding, left_padding, right_padding,
            cv2.BORDER_CONSTANT, value=[0, 0, 0]
        )

        # Set the mock return value for copyMakeBorder
        mock_copyMakeBorder.return_value = expected_padded_image

        # Call the padder function
        padded_image = processor.padder(test_image)

        self.assertTrue(np.array_equal(padded_image, expected_padded_image))
        #
        # self.assertEqual(padded_image.shape[0] % patch_size, 0)
        # self.assertEqual(padded_image.shape[1] % patch_size, 0)



    #### CREATING PATCHES FUNCTIONS ######
    @patch('src.data.data_preprocessing.os.listdir')
    @patch('src.data.data_preprocessing.cv2.imread')
    @patch('src.data.data_preprocessing.cv2.imwrite')
    @patch('src.data.data_preprocessing.patchify')
    @patch('src.data.data_preprocessing.DataPipelineSetup.padder')
    def test_img_patchify(self, mock_padder, mock_patchify, mock_imwrite, mock_imread, mock_listdir):
        # Setup mock return values
        mock_listdir.return_value = ['image1.tif', 'image2.png']
        mock_imread.return_value = MagicMock()
        mock_padder.return_value = MagicMock()
        mock_patchify.return_value = MagicMock()

        # Create an instance of DataPipelineSetup
        processor = DataPipelineSetup()

        # Call the img_patchify method
        img_dir = '/path/to/images'
        save_dir = '/path/to/save'
        img, tifs = processor.img_patchify(img_dir, save_dir)
        print("Contents of img list:", img)


        # Assertions
        # expected_processed_images = 2  # Expecting two images to be processed
        # self.assertNotEqual(len(img), 0)
        # self.assertNotEqual(len(tifs), 0)


    ## OLD TEST ###
    # @patch('os.listdir')
    # @patch('cv2.imread')
    # @patch('cv2.imwrite')
    # @patch('logging.info')
    # @patch('logging.error')    
    # def test_img_patchify(self, mock_logging_error, mock_logging_info, mock_imwrite, mock_imread, mock_listdir):
    #     mock_listdir.return_value = ['test_image.png', 'test_image.tif']
    #     mock_imread.side_effect = [
    #         np.random.randint(0, 256, (500, 500, 3), dtype=np.uint8),
    #         np.random.randint(0, 256, (500, 500), dtype=np.uint8)
    #     ]

    #     processor = DataPipelineSetup()
    #     processor.img_patchify('img_dir', 'save_dir')

    #     self.assertTrue(mock_imwrite.call_count > 0)
    #     mock_logging_error.assert_called_once_with("Error processing test_image.tif: `window_shape` is incompatible with `arr_in.shape`")


   


if __name__ == '__main__':
    unittest.main()
