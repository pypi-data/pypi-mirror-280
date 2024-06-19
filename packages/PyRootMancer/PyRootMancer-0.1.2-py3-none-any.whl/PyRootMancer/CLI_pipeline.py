import os
import typer
import logging
from pathlib import Path

# from src.features.instance_segmentation import InstanceSegmentation from
# src.features.root_coord_extraction import LandmarkExtraction from
# src.data.data_preprocessing import DataPipelineSetup
from models.model_training import ModelTraining

# from src.utils.configuration import folder_config

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.basicConfig(level=logging.INFO)

# %%

app = typer.Typer()


#
# @app.command() def crop(image_folder: Path =
# typer.Option(folder_config.get("images_folder_unpatched"),help="Path to the
# train raw(unpatched) folder images")):
#
#     processor = DataPipelineSetup()
#     processor.crop(str(image_folder))
#
#
#
# @app.command() def img_patchify(image_folder_unpatched: Path =
# typer.Option(folder_config.get("images_folder_unpatched"), help="Path to the
#                  train raw(unpatched) folder images"), image_folder_patched:
#                  Path =
#                  typer.Option(folder_config.get("images_folder_patched"),
#                  help="Path to the train patches folder images (where the
#                  patches need to be saved)")):
#
#     processor = DataPipelineSetup()
#     processor.img_patchify(str(image_folder_unpatched),
# str(image_folder_patched))
#
#


@app.command()
def data_generator(
    images_folder: Path = typer.Option(
        ...,
        help=("Path to the images patches folder, format - 'image_folder/class'"),
    ),
    masks_folder: Path = typer.Option(
        ...,
        help="Path to the masks patches folder, format - 'mask_folder/class'",
    ),
):

    modelling = ModelTraining()
    modelling.data_generator(str(images_folder), str(masks_folder))


@app.command()
def test_job():
    logging.info("IF THIS TEXT IS DISPLAYED THIS JOB IS WORKING")
    pass


#
#
# @app.command() def training_script(epochs: int = typer.Option
# (5, help="Numbers
# of Epochs"), images_folder: Path =
# typer.Option(os.path.dirname(folder_config.get("images_folder_patched")),
#                     help="Path to the images patches folder, format -
#                     'image_folder/class''"), masks_folder: Path =
#                     typer.Option(os.path.dirname(folder_config.get("root_folder_patched")),
#                     help="Path to the images patches folder, format -
#                     'mask_folder/class''"), model_folder: Path =
#                     typer.Option(folder_config.get("models_folder"),
#                     help="Path to the model folder"), model_name: str =
#                     typer.Option("your_model", help="Name your model without
#                     extension")):
#
#     modelling = ModelTraining()
#     trained_model = modelling.training(int(epochs), str(images_folder),
# str(masks_folder), str(model_folder), str(model_name)) if trained_model is
# not
# None:
#
#     # Log and register the model with MLflow
#     mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "databricks"))
#     with mlflow.start_run() as run:
#         # model_path = os.path.join(model_folder, f'{model_name}.keras')
#         mlflow.keras.log_model(trained_model, artifact_path="test_model")
#
#         logging.info(f"Model registered with run ID: {run.info.run_id}")

#
# @app.command() def predict_image(image_path: Path =
# typer.Option(os.path.join(folder_config.get("test_folder"),
#                   "038_43-18-ROOT1-2023-08-08_pvd_OD01_Col0_05-Fish Eye
#                   Corrected.png"), help="Path to an image"), ouput_folder:
#                   Path =
#                   typer.Option(folder_config.get("external_data_folder"),
#                   help="Path to where the prediction should be stored"),
#                   model_folder: Path =
#                   typer.Option(folder_config.get("models_folder"), help="Path
#                   to the model folder"), model_name: str =
#                   typer.Option("best_model_root_masks", help="Model name only
#                   without extension")):
#
#     modelling = ModelTraining()
#     modelling.predict_image(str(image_path), str(ouput_folder),
#     str(model_folder), str(model_name))
#     typer.echo(f"Predicted mask saved to {ouput_folder}")
#
#
# @app.command() def predict_folder(input_folder: Path =
# typer.Option(folder_config.get("test_folder"),help="Path to the images
#                    folder"), output_folder: Path =
#                    typer.Option(folder_config.get("data_predictions"),help="Path
#                    to where the predicted masks should be stored"),
#                    model_folder: Path =
#     typer.Option(folder_config.get("models_folder"),help="Path to the model
#     folder"), model_name: str = typer.Option("best_model_root_masks",
#     help="Model name only without extension")): modelling = ModelTraining()
#     modelling.predict_folder(str(input_folder), str(output_folder),
#     str(model_folder), str(model_name)) typer.echo(f"Predicted masks saved to
#     {output_folder}")
#
#
# @app.command() def return_to_original_size(predicted_raw_folder: Path =
# typer.Option(folder_config.get("data_predictions"),help="Path to the raw
#                             predictions (cropped images)"), output_folder:
#     Path = typer.Option(folder_config.get("data_predictions_clean"),
#     help="Path to the folder where the raw predicted images will be
#     modified")): segmentation = InstanceSegmentation()
#     segmentation.return_original_size_folder(str(predicted_raw_folder),
#     str(output_folder))
#
#
#
# @app.command() def display_prediction(image_path: Path =
# typer.Option(os.path.join(folder_config.get("test_folder"),"035_43-17-ROOT1-2023-08-08_mock_pH5_+Fe_Col0_04-Fish
#                        Eye Corrected.png"), help="Path to an image"),
#                        output_folder: Path =
#                        typer.Option(folder_config.get("external_data_folder"),
#     help="Path to where the prediction should be stored"), model_folder: Path
#     = typer.Option(folder_config.get("models_folder"),help="Path to the model
#     folder"), model_name: str = typer.Option("best_model_root_masks",
#     help="Model name only without extension")): segmentation =
#     InstanceSegmentation() segmentation.test_overlaying(str(image_path),
#     str(output_folder), str(model_folder), str(model_name))
#
#
# @app.command() def display_root_landmarks(predicted_clean_folder: Path =
# typer.Option(folder_config.get("data_predictions_clean"),help="Path to the
#                            clean predicted images folder"), images_folder:
#                            Path =
#     typer.Option(folder_config.get("test_folder"), help="Path to the raw test
#     images"), num_image: int = typer.Option(29, help="num image 0=> <30")):
#     landmarks = LandmarkExtraction()
#     landmarks.display_root_landmarks(str(predicted_clean_folder),
#     str(images_folder), int(num_image))
#


if __name__ == "__main__":
    app()
