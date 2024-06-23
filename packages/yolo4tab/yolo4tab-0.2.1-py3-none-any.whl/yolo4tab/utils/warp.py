import os
from typing import List

import cv2
import numpy as np
import torch
from tqdm import tqdm
from ultralytics import YOLO


def crop_rotate_bbox(img: np.ndarray, corners: np.ndarray) -> np.ndarray:
    corners = corners.astype(np.float32)
    assert len(corners) == 4, "Shape of points must be 4*2"
    img_crop_width = int(
        max(
            np.linalg.norm(corners[0] - corners[1]),
            np.linalg.norm(corners[2] - corners[3]),
        )
    )
    img_crop_height = int(
        max(
            np.linalg.norm(corners[0] - corners[3]),
            np.linalg.norm(corners[1] - corners[2]),
        )
    )
    pts_std = np.float32(
        [
            [0, 0],
            [img_crop_width, 0],
            [img_crop_width, img_crop_height],
            [0, img_crop_height],
        ]
    )
    M = cv2.getPerspectiveTransform(corners, pts_std)
    img_crop = cv2.warpPerspective(
        img,
        M,
        (img_crop_width, img_crop_height),
        borderMode=cv2.BORDER_REPLICATE,
        flags=cv2.INTER_CUBIC,
    )
    return img_crop, M


def crop_segmentation(img: np.ndarray, corners: np.ndarray):
    # Sorting follow ABCD
    x_sorted = sorted(corners, key=lambda point: point[0])
    left_most = x_sorted[:2]
    right_most = x_sorted[2:]

    left_most = sorted(left_most, key=lambda point: point[1])
    right_most = sorted(right_most, key=lambda point: point[1])

    quad_points = np.array(
        [left_most[0], right_most[0], right_most[1], left_most[1]], dtype=np.float32
    )

    # Find rectangle transform
    img_crop_width = np.linalg.norm(quad_points[0] - quad_points[1]).astype(np.int32)
    img_crop_height = np.linalg.norm(quad_points[0] - quad_points[3]).astype(np.int32)
    rect_points = np.array(
        [
            [0, 0],
            [img_crop_width, 0],
            [img_crop_width, img_crop_height],
            [0, img_crop_height],
        ],
        np.float32,
    )

    # Get matrix M and transform image
    M = cv2.getPerspectiveTransform(quad_points, rect_points)
    img_crop = cv2.warpPerspective(
        img.copy().astype(np.float32), M, (img_crop_width, img_crop_height)
    )

    return img_crop, M


def find_approximate_polygon(segment, epsilon_ratio=0.016):
    epsilon = epsilon_ratio * cv2.arcLength(segment, True)
    approx = cv2.approxPolyDP(segment, epsilon, True)
    approx = approx.reshape(-1, 2)

    return approx


def find_bbox(segment):
    bounding_box = cv2.minAreaRect(segment)
    points = sorted(cv2.boxPoints(bounding_box).tolist(), key=lambda x: x[0])

    if points[1][1] > points[0][1]:
        index_1 = 0
        index_4 = 1
    else:
        index_1 = 1
        index_4 = 0
    if points[3][1] > points[2][1]:
        index_2 = 2
        index_3 = 3
    else:
        index_2 = 3
        index_3 = 2

    # return a numpy array of shape (4, 2) with the order of points is top-left, top-right, bottom-right, bottom-left
    return np.array(
        [points[index_1], points[index_2], points[index_3], points[index_4]]
    )


def extend_polygon(polygon, img_width, img_height, padding=20):
    center = np.mean(polygon, axis=0)
    vectors = polygon - center

    lengths = np.linalg.norm(vectors, axis=1)
    scaled_vectors = vectors + vectors * (padding / lengths)[:, np.newaxis]
    expanded_polygon = center + scaled_vectors

    expanded_polygon = np.reshape(expanded_polygon, (-1, 2)).astype(np.int32)

    for p in expanded_polygon:
        p[0] = min(max(p[0], 0), img_width - 1)
        p[1] = min(max(p[1], 0), img_height - 1)

    return expanded_polygon


if __name__ == "__main__":
    # Load a model
    weight = "/home/manhckv/manhckv/ultralytics/runs/train/exp1/weights/best.pt"
    model = YOLO(weight)

    # test_img_dir = "/home/manhckv/manhckv/ultralytics/test"
    test_img_dir = "/home/manhckv/manhckv/ultralytics/td_test"
    # test_img_dir = "/home/manhckv/manhckv/ultralytics/fqa_test"

    output_dir = "_output"
    os.makedirs(output_dir, exist_ok=True)

    for img_file in tqdm(os.listdir(test_img_dir)):
        img_path = os.path.join(test_img_dir, img_file)
        img = cv2.imread(img_path)

        pred = model.predict(img_path, device="3", conf=0.6, iou=0.7)

        result = pred[0]

        if result.masks is None:
            print(f"No object detected in {img_file}")
            continue

        mask = result.masks.xy
        # img = visualize_segments(img, mask)

        corners = []

        crop_imgs = []

        for segment in mask:
            approx_poly = find_approximate_polygon(
                segment
            )  # np.array with shape (4, 2)
            if len(approx_poly) == 4:
                # when can find 4 corners, we can use it directly
                approx_poly = extend_polygon(approx_poly, img.shape[1], img.shape[0])
                corners.append(approx_poly)
                crop_img, _ = crop_segmentation(img, approx_poly)
                crop_imgs.append(crop_img)

            else:
                # else, we need to find the bounding box of the segment
                approx_bbox = find_bbox(segment)
                approx_bbox = extend_polygon(approx_bbox, img.shape[1], img.shape[0])
                corners.append(approx_bbox)
                crop_img, _ = crop_segmentation(img, approx_bbox)
                crop_imgs.append(crop_img)

        # img = plot_4_corner(img, corners)
        # cv2.imwrite(os.path.join(output_dir, img_file), img)
        for idx, crop_img in enumerate(crop_imgs):
            cv2.imwrite(os.path.join(output_dir, f"{img_file}_{idx}.jpg"), crop_img)
