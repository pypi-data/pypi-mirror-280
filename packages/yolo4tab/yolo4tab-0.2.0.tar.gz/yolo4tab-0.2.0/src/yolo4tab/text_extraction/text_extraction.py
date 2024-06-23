from typing import Dict, Union

import cv2
import easyocr
import numpy as np


class TextExtraction:
    def __init__(self, languages=['vi', 'en'], use_gpu=False):
        self.reader = easyocr.Reader(languages, gpu=use_gpu)

    def extract_text(self, image_source: Union[str, np.ndarray]) -> Dict:
        assert isinstance(image_source, np.ndarray) or isinstance(
            image_source, str
        ), "Image source must be a string or a numpy array."

        if isinstance(image_source, str):
            image = cv2.imread(image_source)

        else:
            image = image_source

        results = self.reader.readtext(image)
        final_results = []
        for bbox, text, _ in results:
            final_results.append(
                {
                    'bbox': [
                        int(bbox[0][0]),
                        int(bbox[0][1]),
                        int(bbox[2][0]),
                        int(bbox[2][1]),
                    ],
                    'text': text,
                    'center': [
                        int((bbox[0][0] + bbox[2][0]) / 2),
                        int((bbox[0][1] + bbox[2][1]) / 2),
                    ],
                }
            )

        return final_results
