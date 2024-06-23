from typing import Dict, List, Union

import numpy as np
from PIL import Image

from .const import BorderFormat, HorizontalAlign, OutputFormat, VerticalAlign
from .table_detection.table_detection import TableDetection
from .table_reconstruction.table_reconstruction import TableReconstruction
from .table_structure_recognition.table_structure_recognition import (
    TableStructureRecognition,
)
from .text_extraction.text_extraction import TextExtraction


class TableExtraction:

    def __init__(
        self, td_weight_path: str = None, tsr_weight_path: str = None, device="cpu"
    ):
        """Initialize TableExtraction class.

        Args:
            td_weight_path (str, optional): Path to table detection weight. Defaults to None (use default weight).
            tsr_weight_path (str, optional): Path to table structure recognition weight. Defaults to None (use default weight).
            device (str, optional): Device to run the model. Defaults to "cpu".
        """

        ## Initialize components
        self.table_detection = TableDetection(weight_path=td_weight_path, device=device)
        self.table_structure_recognition = TableStructureRecognition(
            weight_path=tsr_weight_path, device=device
        )

        ## NOTE: EasyOCR only run on card 0, to prevent error, set use_gpu=False
        self.text_extraction = TextExtraction(
            # use_gpu=False if device == "cpu" else True
            use_gpu=False
        )
        self.table_reconstruction = TableReconstruction()
        self.default_hparams = {
            "td": {
                "conf": 0.7,
                "iou": 0.4,
                "extend_ratio": 0.12,
                "padding": 40,
            },
            "tsr": {
                "conf": 0.25,
                "iou": 0.5,
            },
        }

    def extract_table(
        self,
        image_source: Union[str, np.ndarray, Image.Image],
        output_formats: List[OutputFormat] = [
            OutputFormat.CSV,
            OutputFormat.HTML,
            OutputFormat.LATEX,
        ],
        border_format: BorderFormat = BorderFormat.FULL_BORDER,
        vertical_align: VerticalAlign = VerticalAlign.MIDDLE,
        horizontal_align: HorizontalAlign = HorizontalAlign.LEFT,
    ) -> List[Dict]:
        """Extract tables from the input image source.

        Args:
            image_source (Union[str, np.ndarray, Image.Image]): Input image source. It can be a file path, numpy array, or PIL Image.
            crop_padding (int, optional): Padding for cropping the detected tables. Defaults to 10.
            output_formats (List[OutputFormat], optional): Output formats for the reconstructed tables. Defaults to output all formats.
            border_format (BorderFormat, optional): Border format for the reconstructed tables. Defaults to BorderFormat.FULL_LINE.
            vertical_align (VerticalAlign, optional): Vertical align for the reconstructed tables. Defaults to VerticalAlign.MIDDLE.
            horizontal_align (HorizontalAlign, optional): Horizontal align for the reconstructed tables. Defaults to HorizontalAlign.LEFT.

        Returns:
            List[Dict]: List of detected tables with the reconstructed table string.
        """
        ## Step 1: Detect tables
        detected_tables = self.table_detection.process(
            image_source=image_source,
            conf=self.default_hparams["td"]["conf"],
            iou=self.default_hparams["td"]["iou"],
            extend_ratio=self.default_hparams["td"]["extend_ratio"],
            padding=self.default_hparams["td"]["padding"],
        )

        fail_tables = []

        ## Step 2: Extract table structure and values
        for table in detected_tables:

            ### Step 2.1: Table structure recognition
            table_image = table["table_image"]
            table_structure = self.table_structure_recognition.process(
                image_source=table_image,
                conf=self.default_hparams["tsr"]["conf"],
                iou=self.default_hparams["tsr"]["iou"],
            )

            if (
                table_structure is None
                or table_structure["num_rows"] == 0
                or table_structure["num_columns"] == 0
                or len(table_structure["cells"]) == 0
            ):
                fail_tables.append(table["table_id"])
                continue

            ### Step 2.2: Text extraction
            table_values = self.text_extraction.extract_text(table_image)

            ### Step 2.3: Table reconstruction
            table_outputs = self.table_reconstruction.process(
                table_structure=table_structure,
                table_values=table_values,
                output_formats=output_formats,
                border_format=border_format,
                vertical_align=vertical_align,
                horizontal_align=horizontal_align,
            )

            table["table_structure"] = table_structure
            table["table_values"] = table_values
            table["outputs"] = table_outputs["outputs"]

        ## Step 3: Remove fail tables
        detected_tables = [
            table for table in detected_tables if table["table_id"] not in fail_tables
        ]
        return detected_tables
