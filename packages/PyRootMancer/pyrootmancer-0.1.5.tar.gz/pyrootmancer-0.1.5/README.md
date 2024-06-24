
# PyRootMancer - Root Segmentation Project

Welcome to PyRootMancer, the magical tool for all your root segmentation needs! 🌱✨ Whether you're a plant physiologist, agronomist, or ecologist, PyRootMancer is here to help you unravel the mysteries of root systems with the power of deep learning.

Harnessing the enchanting capabilities of the U-Net model architecture, PyRootMancer ensures that your root images are segmented with pinpoint accuracy. This wizardry not only facilitates precise detection and segmentation of root structures but also aids in comprehensive analyses and research.

Root system analysis has never been this easy and fun! By automating the segmentation process, PyRootMancer allows you to efficiently process large datasets, extract meaningful data, and conduct thorough analyses with minimal manual intervention. Get ready to streamline your workflow, enhance segmentation accuracy, and accelerate your discoveries in plant science.


## Table of Contents
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Authors](#authors)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/BredaUniversityADSAI/2023-24d-fai2-adsai-group-cv5.git
    ```
2. Navigate to the project directory:
    ```sh
    cd 2023-24d-fai2-adsai-group-cv5
    ```
3. Install Poetry if you haven't already:
    ```sh
    pip install poetry
    ```
4. Install the project dependencies:
    ```sh
    poetry install
    ```
5. Activate the virtual environment:
    ```sh
    poetry shell
    ```

Alternatively, you can install PyRootMancer using pip:

```sh
pip install pyrootmancer
```

## Dependencies

The project dependencies are managed using Poetry. Below is a list of key dependencies:

- tensorflow-io-gcs-filesystem: `0.30.0`
- tensorflow: `2.16.1`
- tensorflow-intel: `2.16.1`
- opencv-python: `^4.9.0.80`
- pandas: `^2.2.2`
- patchify: `^0.2.3`
- matplotlib: `^3.8.4`
- scikit-image: `^0.23.2`
- skan: `^0.11.1`
- numpy: `1.23.5`
- pytest: `^8.2.0`
- pytest-mock: `^3.14.0`
- sphinx: `^7.3.7`
- coverage: `^7.5.3`
- sphinx_rtd_theme: `2.0.0`
- networkx: `^3.3`

For a complete list of dependencies, refer to the `pyproject.toml` file.

## Usage

### Data Preprocessing

The `DataPipelineSetup` class handles data preprocessing tasks such as creating folders, unzipping files, cropping images, and patchifying images.

Example usage:
```python
from src.data.data_preprocessing import DataPipelineSetup

processor = DataPipelineSetup()
processor.create_folders()
processor.unzip("train")
processor.unzip("test")
processor.unzip("masks")
processor.crop("path/to/folder")
processor.img_patchify("path/to/img_dir", "path/to/save_dir")
```

### Model Training

The `ModelTraining` class handles the training of the U-Net model for image segmentation.

Example usage:
```python
from src.models.model_training import ModelTraining

trainer = ModelTraining()
trainer.training(epochs=10, image_folder="path/to/images", mask_folder="path/to/masks", model_folder="path/to/models", model_name="unet_model")
```

### Instance Segmentation

The `InstanceSegmentation` class performs instance segmentation tasks including noise removal, overlaying masks, and resizing predicted masks to match the size of original images.

Example usage:

```python
from src.features.instance_segmentation import InstanceSegmentation

segmenter = InstanceSegmentation()

# Perform noise removal on an image
clean_image = segmenter.opening_closing(image)

# Overlay a predicted mask on a test image
blended_image = segmenter.test_overlaying(image_path="path/to/image.png", output_folder="path/to/output", model_folder="path/to/model", model_name="model_name")

# Resize predicted masks to match original image size and overlay them
resized_image = segmenter.return_original_size_image(image_path="path/to/image.png", output_folder="path/to/output")
```

### Root Coordinate Extraction

The LandmarkExtraction class extracts landmarks and coordinates from root images, processes and filters them based on certain criteria.

Example usage:

```python
from src.features.root_coord_extraction import LandmarkExtraction

extractor = LandmarkExtraction()

# Remove small components from a mask
clean_mask = extractor.remove_small_components(mask)

# Get bottom coordinates of roots in an image
coords_0, coords_1 = extractor.get_bottom_coordinates(input_folder="path/to/input", num_img=0)

# Display root landmarks on an image
extractor.display_root_landmarks(input_folder="path/to/input", test_folder="path/to/test", num_img=0)
```

### Root Length Calculation

The RootLengthCalculator class calculates the length of roots from segmented images using a trained model.

Example usage:

```python
from src.features.root_length import RootLengthCalculator
from src.models.model_evaluation import f1, iou

img_dir = "path/to/images"
model_path = "path/to/model"
custom_objects = {"f1": f1, "iou": iou}
csv_filename = "path/to/results.csv"

calculator = RootLengthCalculator(img_dir, model_path, custom_objects)
calculator.process_images()
calculator.save_results(csv_filename)
```

### Model Evaluation

The `model_evaluation.py` script provides functions for calculating F1 score and Intersection over Union (IoU).

Example usage:
```python
from src.models.model_evaluation import f1, iou
```

### Configuration

The `configuration.py` script provides the folder and parameter configurations used throughout the project.

## Project Structure
```
2023-24d-fai2-adsai-group-cv5/
├── data/
│   ├── external/
│   ├── processed/
│   ├── data_predictions
│   ├── data_predictions_clean
│   └── raw/
│       ├── data_unpatched/
│       └── data_patched/
├── models/
│   └── best_model
├── src/
│   ├── data/
│   │   └── data_preprocessing.py
│   ├── features/
│   │   ├── instance_segmentation.py
│   │   ├── root_coord_extraction.py
│   │   └── root_length.py
│   ├── models/
│   │   ├── model_definitions.py
│   │   ├── model_evaluation.py
│   │   └── model_training.py
│   ├── utils/
│   │   └── configuration.py
├── README.md
└── pyproject.toml
```

## Authors

- Simona Dimitrova (222667@buas.nl) - `data_preprocessing.py`
- Jakub Cyba (223860@buas.nl) - `model_training.py`
- Cédric Verhaegh (221350@buas.nl) - `instance_segmentation.py`
- Thomas Pichardo (223834@buas.nl) - `root_coord_extraction.py`
- Samuel Vieira Vasconcelos (211941@buas.nl) - `root_length.py`

