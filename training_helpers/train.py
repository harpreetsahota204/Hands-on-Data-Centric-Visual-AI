"""
This script is used to train the model for the project.

You should import your main functions from the data_curation.py script and use them to prepare the dataset for training.

The approved model is `yolov8m` from Ulytralytics. 

Your predictions must be in a label_field called "predictions" in the dataset.

You may pass your final selection of hyperparameters as keyword arguments in the load_zoo_model function. 

See here for more details about hyperparameters for this model: https://docs.ultralytics.com/modes/train/#train-settings

"""
import os
from datetime import datetime
import yaml
from pathlib import Path
import shutil

import fiftyone as fo
import fiftyone.utils.random as four

from ultralytics import YOLO

def export_to_yolo_format(
    samples,
    classes,
    label_field="ground_truth",
    export_dir="./yolo_formatted",
    splits=["train", "val"]
):
    """
    Export samples to YOLO format, optionally handling multiple data splits.

    Args:
        samples (fiftyone.core.collections.SampleCollection): The dataset or samples to export.
        export_dir (str): The directory where the exported data will be saved.
        classes (list): A list of class names for the YOLO format.
        label_field (str, optional): The field in the samples that contains the labels.
            Defaults to "ground_truth".
        splits (str, list, optional): The split(s) to export. Can be a single split name (str) 
            or a list of split names. If None, all samples are exported as "val" split. 
            Defaults to None.

    Returns:
        None

    """
    if splits is None:
        splits = ["val"]
    elif isinstance(splits, str):
        splits = [splits]

    for split in splits:
        split_view = samples if split == "val" and splits == ["val"] else samples.match_tags(split)
        
        split_view.export(
            export_dir=export_dir,
            dataset_type=fo.types.YOLOv5Dataset,
            label_field=label_field,
            classes=classes,
            split=split
        )

def train_model(training_dataset, training_config):
    """
    Train the YOLO model on the given dataset using the provided configuration.
    """
    four.random_split(training_dataset, {"train": training_config['train_split'], "val": training_config['val_split']})
    
    print("Exporting dataset to YOLO format...")

    export_to_yolo_format(
        samples=training_dataset,
        classes=training_dataset.default_classes,
    )
    print("Dataset exported to YOLO format.")

    print("Loading the model...")

    model = YOLO("yolov8m.pt")

    print("Training the model...")

    results = model.train(
        data="./yolo_formatted/dataset.yaml",
        **training_config['train_params']
    )
    
    print("Training complete. Loading best model")

    best_model_path = str(results.save_dir / "weights/best.pt")
    best_model = YOLO(best_model_path)

    return best_model

def run_inference_on_eval_set(eval_dataset, best_model):
    """
    Run inference on the evaluation set using the best trained model.

    Args:
        eval_dataset (fiftyone.core.dataset.Dataset): The evaluation dataset.
        best_model (YOLO): The best trained YOLO model.

    Returns:
        The dataset eval_dataset with predictions
    """
    print("Running inference on the evaluation dataset...")
    
    eval_dataset.apply_model(best_model, label_field="predictions")
    eval_dataset.save()

    print("Inference complete.")
    return eval_dataset


def eval_model(dataset_to_evaluate):
    """
    Evaluate the model on the evaluation dataset.

    Args:
        dataset_to_evaluate (fiftyone.core.dataset.Dataset): The evaluation dataset.

    Returns:
        the mean average precision (mAP) of the model on the evaluation dataset.
    """
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    print("Evaluating the model...")

    detection_results = dataset_to_evaluate.evaluate_detections(
        gt_field="ground_truth",  
        pred_field="predictions",
        eval_key=f"evalrun_{current_datetime}",
        compute_mAP=True,
        )
    
    print("Evaluation complete.")

    return detection_results

def run(train_dataset, eval_dataset, training_config):
    """
    Main function to run the entire training and evaluation process.

    Returns:
        model_results: a fiftyone.utils.eval.detection.DetectionResults object
    """

    print("Loading configuration file ...")

    script_dir = Path(__file__).resolve().parent
    config_path = script_dir / 'training_config.yaml'
    with config_path.open('r') as file:
        training_config = yaml.safe_load(file)

    best_trained_model = train_model(training_dataset=train_dataset, training_config=training_config)
    
    model_predictions = run_inference_on_eval_set(eval_dataset=eval_dataset, best_model=best_trained_model)
    
    results = eval_model(dataset_to_evaluate=model_predictions)

    print("Cleaning up YOLO formatted dataset...")

    path_to_remove = script_dir / "yolo_formatted"

    if path_to_remove.exists():
        shutil.rmtree(path_to_remove)
        print(f"Removed {path_to_remove}")
    else:
        print(f"Directory {path_to_remove} does not exist.")

    return results