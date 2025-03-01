import argparse
import os
import sys

from PyQt5.QtWidgets import QApplication

from salt.editor import Editor
from salt.interface import ApplicationInterface

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--onnx-models-path", type=str, default="./models")
    parser.add_argument("--dataset-path", type=str, default="./dataset")
    parser.add_argument("--categories", type=str)
    parser.add_argument("--from-start", type=bool, default=False, help="Start from the beginning of the dataset (if you've already started annotating)")
    args = parser.parse_args()

    onnx_models_path = args.onnx_models_path
    dataset_path = args.dataset_path
    categories = None
    if args.categories is not None:
        categories = args.categories.split(",")

    coco_json_path = os.path.join(dataset_path, "annotations.json")

    editor = Editor(
        onnx_models_path,
        dataset_path,
        categories=categories,
        coco_json_path=coco_json_path
    )

    app = QApplication(sys.argv)
    window = ApplicationInterface(app, editor)
    window.show()
    sys.exit(app.exec_())
