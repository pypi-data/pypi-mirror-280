from typing import Dict, List, Union
from uuid import uuid4

import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

from ..const import TD_VERSION, Task
from ..utils.general import verify_device, verify_weight
from ..utils.warp import (
    crop_rotate_bbox,
    crop_segmentation,
    extend_polygon,
    find_approximate_polygon,
    find_bbox,
)


class TableDetection:
    def __init__(
        self,
        weight_path: str = None,
        device: str = "cpu",
    ):
        """Initialize TableDetection module

        Args:
            weight_path (str): Path to the weight file. Defaults to None (use default weight).
            device (str, optional): Device to run the model. Defaults to "cpu".
        """
        device = verify_device(device)
        self.weight_path = verify_weight(weight_path, Task.TABLE_DETECTION, TD_VERSION)
        self.model = YOLO(self.weight_path).to(device)

    def process(
        self,
        image_source: Union[str, np.ndarray, Image.Image],
        conf: float = 0.25,
        iou: float = 0.7,
        extend_ratio: float = 0.1,
        padding: int = 10,
    ) -> List[Dict]:
        """Perform table detection on the input image source

        Args:
            image_source (Union[str, np.ndarray, Image.Image]): Input image source. Can be path to image file, numpy array or PIL Image.
            conf (float, optional): Confidence threshold. Defaults to 0.25.
            iou (float, optional): IOU threshold. Defaults to 0.7.
            extend_ratio (float, optional): Ratio for extending the detected table based on smallest dimension of the table bbox. Defaults to 0.1.
            padding (int, optional): Size of white padding for cropping the table. Defaults to 10.

        Returns:
            List[Dict]: List of detected tables. Each table is a dictionary with keys: table_id, bbox, mask, score, ultralytics, table_image, approx_poly
        """
        infer_results = self._infer(image_source, conf=conf, iou=iou)

        final_results = []
        for table in infer_results:
            table_bbox = table.boxes.xyxy[0].int().tolist()
            table_segment = table.masks.xy[0].astype(int)
            score = table.boxes.conf.item()
            table_result = {
                "table_id": str(uuid4()),
                "bbox": table_bbox,
                "mask": table_segment,
                "score": score,
                "ultralytics": table,
                "table_image": None,
            }

            if table_segment is not None and table_bbox is not None:
                orig_img = table.orig_img
                height, width = table.orig_shape

                detect_width = table_bbox[2] - table_bbox[0]
                detect_height = table_bbox[3] - table_bbox[1]

                approx_poly = find_approximate_polygon(table_segment)
                if len(approx_poly) == 4:
                    approx_poly = extend_polygon(
                        approx_poly,
                        width,
                        height,
                        padding=extend_ratio * min(detect_width, detect_height),
                    )
                    crop_img, _ = crop_segmentation(orig_img, approx_poly)
                else:
                    approx_bbox = find_bbox(table_segment)
                    approx_bbox = extend_polygon(
                        approx_bbox,
                        width,
                        height,
                        padding=extend_ratio * min(detect_width, detect_height),
                    )
                    crop_img, _ = crop_rotate_bbox(orig_img, approx_bbox)

                crop_img = cv2.copyMakeBorder(
                    crop_img,
                    padding,
                    padding,
                    padding,
                    padding,
                    cv2.BORDER_CONSTANT,
                    value=(255, 255, 255),
                )
                table_result["approx_poly"] = approx_poly
                table_result["table_image"] = crop_img.astype(np.uint8)

            final_results.append(table_result)

        ## Sort by y0 of table bbox, then x0 of table bbox
        final_results = sorted(
            final_results, key=lambda x: (x["bbox"][1], x["bbox"][0])
        )

        return final_results

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
            source=image_source, conf=conf, iou=iou, retina_masks=True, verbose=False
        )
        return results[0]
