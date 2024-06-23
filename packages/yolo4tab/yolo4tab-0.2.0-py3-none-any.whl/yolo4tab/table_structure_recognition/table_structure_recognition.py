from typing import Dict, List, Union

import numpy as np
from fitz import Rect
from PIL import Image
from ultralytics import YOLO

from ..const import TSR_VERSION, Task
from ..utils.common import (
    align_columns,
    align_rows,
    iob,
    refine_columns,
    refine_rows,
    refine_table_structure,
)
from ..utils.general import verify_device, verify_weight


ID_TO_LABEL = {
    0: "table",
    1: "table row",
    2: "table column",
    3: "table spanning cell",
}

CLASS_THRESHOLD = {
    "table": 0.5,
    # "table column": 0.5,
    "table column": 0.25,
    "table row": 0.5,
    "table spanning cell": 0.5,
}


class TableStructureRecognition:
    def __init__(
        self,
        weight_path: str = None,
        device: str = "cpu",
    ):
        """Initialize TableStructureRecognition module

        Args:
            weight_path (str): Path to the weight file. Defaults to None (use default weight).
            device (str, optional): Device to run the model. Defaults to "cpu".
        """
        device = verify_device(device)
        self.weight_path = verify_weight(
            weight_path, Task.TABLE_STRUCTURE_RECOGNITION, TSR_VERSION
        )
        self.model = YOLO(self.weight_path).to(device)

    def process(
        self,
        image_source: Union[str, np.ndarray, Image.Image],
        conf: float = 0.25,
        iou: float = 0.7,
    ) -> Dict:
        """Perform table structure recognition on the input image source

        Args:
            image_source (Union[str, np.ndarray, Image.Image]): Input image source. Can be path to image file, numpy array or PIL Image.
            conf (float, optional): Confidence threshold. Defaults to 0.25.
            iou (float, optional): IOU threshold. Defaults to 0.7.

        Returns:
            Dict: A dictionary containing table structure with keys: table, rows, columns, spanning_cells
        """

        infer_results = self._infer(image_source=image_source, conf=conf, iou=iou)

        table_objects = []
        for tb_object in infer_results:

            object_label = ID_TO_LABEL[int(tb_object.boxes.cls)]
            object_bbox = tb_object.boxes.xyxy[0].int().tolist()
            object_score = float(tb_object.boxes.conf)

            object_result = {
                "label": object_label,
                "bbox": object_bbox,
                "score": object_score,
            }

            table_objects.append(object_result)

        ## Post process to get table structure
        if len(table_objects) == 0:
            return None
        table_structure = self._post_process(table_objects)
        if (
            table_structure is None
            or len(table_structure["rows"]) == 0
            or len(table_structure["columns"]) == 0
        ):
            return None
        table_structure = self._get_cells(table_structure)
        return table_structure

    def _infer(
        self,
        image_source: Union[str, np.ndarray, Image.Image],
        conf: float = 0.25,
        iou: float = 0.7,
    ) -> List:
        """Perform inference on the input image source

        Args:
            image_source (Union[str, np.ndarray, Image.Image]): Input image source. Can be path to image file, numpy array or PIL Image.
            conf (float, optional): Confidence threshold. Defaults to 0.25.
            iou (float, optional): IOU threshold. Defaults to 0.7.

        Returns:
            List: List of result object defined by Ultralytics
        """
        results = self.model.predict(
            source=image_source, conf=conf, iou=iou, verbose=False
        )
        return results[0]

    def _post_process(
        self, table_objetcs: List[Dict], iob_threshold: float = 0.5
    ) -> Dict:
        """Post process to get table structure

        Args:
            table_objetcs (List[Dict]): List of table objects detected by the model with keys: label, bbox, score.
            iob_threshold (float, optional): IOB threshold. Defaults to 0.5.

        Returns:
            Dict: A dictionary containing table structure with keys: table, rows, columns, spanning_cells.
        """
        ## Step 1 -> Get table bbox
        table = [obj for obj in table_objetcs if obj["label"] == "table"]

        ### If there is no table detected, return None
        if len(table) == 0:
            return None

        ### Else, get the table with highest score
        table = sorted(table, key=lambda x: x['score'], reverse=True)
        table = table[0]

        ## Step 2 -> Get objects in table which iob > iob_threshold
        ## and classifiy them to rows, columns, spanning cells
        table_objects = [
            obj
            for obj in table_objetcs
            if iob(obj['bbox'], table['bbox']) >= iob_threshold
        ]

        ## Step 3: Get row, columns and spaning cells
        rows, columns, spaning_cells = [], [], []
        for obj in table_objects:
            if obj["label"] == "table row":
                rows.append(obj)
            elif obj["label"] == "table column":
                columns.append(obj)
            elif obj["label"] == "table spanning cell":
                spaning_cells.append(obj)

        ### If no rows/columns left, add a row/column based on table bbox
        if len(rows) == 0:
            rows.append(
                {
                    "label": "table row",
                    "bbox": table['bbox'],
                    "score": 1.0,
                }
            )

        if len(columns) == 0:
            columns.append(
                {
                    "label": "table column",
                    "bbox": table['bbox'],
                    "score": 1.0,
                }
            )

        ## Step 4 -> Refine table structures (rows, columns, spanning cells) by NMS threshold
        rows = refine_rows(rows, CLASS_THRESHOLD["table row"])
        columns = refine_columns(columns, CLASS_THRESHOLD["table column"])

        ## Step 5 -> Align rows and columns to fit table bounding box
        row_rect = Rect()
        for obj in rows:
            row_rect.include_rect(obj['bbox'])

        column_rect = Rect()
        for obj in columns:
            column_rect.include_rect(obj['bbox'])

        table['row_column_bbox'] = [
            column_rect[0],
            row_rect[1],
            column_rect[2],
            row_rect[3],
        ]
        table['bbox'] = table['row_column_bbox']

        columns = align_columns(columns, table['row_column_bbox'])
        rows = align_rows(rows, table['row_column_bbox'])

        ## Step 6 -> Get structure
        table_structure = {}
        table_structure['table'] = table
        table_structure['rows'] = rows
        table_structure['columns'] = columns
        table_structure['spanning_cells'] = spaning_cells

        ## Step 7 -> Refine table structure
        if len(rows) > 0 and len(columns) > 1:
            table_structure = refine_table_structure(table_structure, CLASS_THRESHOLD)

        ## Step 8 -> Save result
        return table_structure

    def _get_cells(self, table_structure: Dict) -> List[Dict]:
        """Get list of cells from detected table structure

        Args:
            table_structure (Dict): Table components detected and refined. Dictionary with keys: table, rows, columns, spanning_cells.

        Returns:
            Dict: List of cells in table. Cells are represented by dictionary with keys:
                - bbox: Bounding box of cell
                - column_nums: List of column numbers that cell spans
                - row_nums: List of row numbers that cell spans
        """

        columns = table_structure["columns"]
        rows = table_structure["rows"]
        num_rows = len(rows)
        num_columns = len(columns)
        spanning_cells = table_structure["spanning_cells"]
        cells = []
        subcells = []

        ## Identify complete cells and subcells
        for column_num, column in enumerate(columns):
            for row_num, row in enumerate(rows):
                column_rect = Rect(list(column['bbox']))
                row_rect = Rect(list(row['bbox']))
                cell_rect = row_rect.intersect(column_rect)
                cell = {
                    'bbox': list(cell_rect),
                    'column_nums': [column_num],
                    'row_nums': [row_num],
                }

                cell['subcell'] = False
                for spanning_cell in spanning_cells:
                    spanning_cell_rect = Rect(list(spanning_cell['bbox']))
                    if (
                        spanning_cell_rect.intersect(cell_rect).get_area()
                        / cell_rect.get_area()
                    ) > 0.5:
                        cell['subcell'] = True
                        break

                if cell['subcell']:
                    subcells.append(cell)
                else:
                    cells.append(cell)

        for spanning_cell in spanning_cells:
            spanning_cell_rect = Rect(list(spanning_cell['bbox']))
            cell_columns = set()
            cell_rows = set()
            cell_rect = None
            for subcell in subcells:
                subcell_rect = Rect(list(subcell['bbox']))
                subcell_rect_area = subcell_rect.get_area()
                if (
                    subcell_rect.intersect(spanning_cell_rect).get_area()
                    / subcell_rect_area
                ) > 0.5:
                    if cell_rect is None:
                        cell_rect = Rect(list(subcell['bbox']))
                    else:
                        cell_rect.include_rect(Rect(list(subcell['bbox'])))
                    cell_rows = cell_rows.union(set(subcell['row_nums']))
                    cell_columns = cell_columns.union(set(subcell['column_nums']))

            if len(cell_rows) > 0 and len(cell_columns) > 0:
                cell = {
                    'bbox': list(cell_rect),
                    'column_nums': list(cell_columns),
                    'row_nums': list(cell_rows),
                }
                cells.append(cell)

        dilated_columns = columns
        dilated_rows = rows
        for cell in cells:
            column_rect = Rect()
            for column_num in cell['column_nums']:
                column_rect.include_rect(list(dilated_columns[column_num]['bbox']))
            row_rect = Rect()
            for row_num in cell['row_nums']:
                row_rect.include_rect(list(dilated_rows[row_num]['bbox']))
            cell_rect = column_rect.intersect(row_rect)
            cell['bbox'] = list(cell_rect)

        ## Sort cells from left to right, top to bottom
        sorted_cells = sorted(
            cells, key=lambda cell: (cell['row_nums'][0], cell['column_nums'][0])
        )

        ## Drop 'subcell' key
        for cell in sorted_cells:
            cell.pop('subcell', None)

        table_structure['cells'] = sorted_cells
        table_structure['num_rows'] = num_rows
        table_structure['num_columns'] = num_columns
        return table_structure
