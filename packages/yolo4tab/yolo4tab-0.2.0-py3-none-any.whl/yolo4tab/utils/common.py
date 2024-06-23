from fitz import Rect


def iob(bbox1, bbox2):
    """
    Compute the intersection area over box area, for bbox1.
    """
    intersection = Rect(bbox1).intersect(bbox2)

    bbox1_area = Rect(bbox1).get_area()
    if bbox1_area > 0:
        return intersection.get_area() / bbox1_area

    return 0


def sort_objects_by_score(objects, reverse=True):
    """
    Put any set of objects in order from high score to low score.
    """
    if reverse:
        sign = -1
    else:
        sign = 1
    return sorted(objects, key=lambda k: sign * k['score'])


def sort_objects_left_to_right(objs):
    """
    Put the objects in order from left to right.
    """
    return sorted(objs, key=lambda k: k['bbox'][0] + k['bbox'][2])


def sort_objects_top_to_bottom(objs):
    """
    Put the objects in order from top to bottom.
    """
    return sorted(objs, key=lambda k: k['bbox'][1] + k['bbox'][3])


def nms(
    objects, match_criteria="object2_overlap", match_threshold=0.05, keep_higher=True
):
    """
    A customizable version of non-maxima suppression (NMS).

    Default behavior: If a lower-confidence object overlaps more than 5% of its area
    with a higher-confidence object, remove the lower-confidence object.

    objects: set of dicts; each object dict must have a 'bbox' and a 'score' field
    match_criteria: how to measure how much two objects "overlap"
    match_threshold: the cutoff for determining that overlap requires suppression of one object
    keep_higher: if True, keep the object with the higher metric; otherwise, keep the lower
    """
    if len(objects) == 0:
        return []

    objects = sort_objects_by_score(objects, reverse=keep_higher)

    num_objects = len(objects)
    suppression = [False for obj in objects]

    for object2_num in range(1, num_objects):
        object2_rect = Rect(objects[object2_num]['bbox'])
        object2_area = object2_rect.get_area()
        for object1_num in range(object2_num):
            if not suppression[object1_num]:
                object1_rect = Rect(objects[object1_num]['bbox'])
                object1_area = object1_rect.get_area()
                intersect_area = object1_rect.intersect(object2_rect).get_area()
                try:
                    if match_criteria == "object1_overlap":
                        metric = intersect_area / object1_area
                    elif match_criteria == "object2_overlap":
                        metric = intersect_area / object2_area
                    elif match_criteria == "iou":
                        metric = intersect_area / (
                            object1_area + object2_area - intersect_area
                        )
                    if metric >= match_threshold:
                        suppression[object2_num] = True
                        break
                except Exception:
                    # Intended to recover from divide-by-zero
                    pass

    return [obj for idx, obj in enumerate(objects) if not suppression[idx]]


def apply_threshold(objects, threshold):
    """
    Filter out objects below a certain score.
    """
    return [obj for obj in objects if obj['score'] >= threshold]


def align_supercells(supercells, rows, columns):
    """
    For each supercell, align it to the rows it intersects 50% of the height of,
    and the columns it intersects 50% of the width of.
    Eliminate supercells for which there are no rows and columns it intersects 50% with.
    """
    aligned_supercells = []

    for supercell in supercells:
        row_bbox_rect = None
        col_bbox_rect = None
        intersecting_data_rows = set()
        for row_num, row in enumerate(rows):
            row_height = row['bbox'][3] - row['bbox'][1]
            supercell_height = supercell['bbox'][3] - supercell['bbox'][1]
            min_row_overlap = max(row['bbox'][1], supercell['bbox'][1])
            max_row_overlap = min(row['bbox'][3], supercell['bbox'][3])
            overlap_height = max_row_overlap - min_row_overlap
            if 'span' in supercell:
                overlap_fraction = max(
                    overlap_height / row_height, overlap_height / supercell_height
                )
            else:
                overlap_fraction = overlap_height / row_height
            if overlap_fraction >= 0.5:
                intersecting_data_rows.add(row_num)

        intersecting_rows = intersecting_data_rows
        # Determine vertical span of aligned supercell
        for row_num in intersecting_rows:
            if row_bbox_rect is None:
                row_bbox_rect = Rect(rows[row_num]['bbox'])
            else:
                row_bbox_rect = row_bbox_rect.include_rect(rows[row_num]['bbox'])
        if row_bbox_rect is None:
            continue

        intersecting_cols = []
        for col_num, col in enumerate(columns):
            col_width = col['bbox'][2] - col['bbox'][0]
            supercell_width = supercell['bbox'][2] - supercell['bbox'][0]
            min_col_overlap = max(col['bbox'][0], supercell['bbox'][0])
            max_col_overlap = min(col['bbox'][2], supercell['bbox'][2])
            overlap_width = max_col_overlap - min_col_overlap
            if 'span' in supercell:
                overlap_fraction = max(
                    overlap_width / col_width, overlap_width / supercell_width
                )
            else:
                overlap_fraction = overlap_width / col_width
            if overlap_fraction >= 0.5:
                intersecting_cols.append(col_num)
                if col_bbox_rect is None:
                    col_bbox_rect = Rect(col['bbox'])
                else:
                    col_bbox_rect = col_bbox_rect.include_rect(col['bbox'])
        if col_bbox_rect is None:
            continue

        supercell_bbox = list(row_bbox_rect.intersect(col_bbox_rect))
        supercell['bbox'] = supercell_bbox

        # Only a true supercell if it joins across multiple rows or columns
        if (
            len(intersecting_rows) > 0
            and len(intersecting_cols) > 0
            and (len(intersecting_rows) > 1 or len(intersecting_cols) > 1)
        ):
            supercell['row_numbers'] = list(intersecting_rows)
            supercell['column_numbers'] = intersecting_cols
            aligned_supercells.append(supercell)

    return aligned_supercells


def nms_supercells(supercells):
    """
    A NMS scheme for supercells that first attempts to shrink supercells to
    resolve overlap.
    If two supercells overlap the same (sub)cell, shrink the lower confidence
    supercell to resolve the overlap. If shrunk supercell is empty, remove it.
    """

    supercells = sort_objects_by_score(supercells)
    num_supercells = len(supercells)
    suppression = [False for supercell in supercells]

    for supercell2_num in range(1, num_supercells):
        supercell2 = supercells[supercell2_num]
        for supercell1_num in range(supercell2_num):
            supercell1 = supercells[supercell1_num]
            remove_supercell_overlap(supercell1, supercell2)
        if (
            (
                len(supercell2['row_numbers']) < 2
                and len(supercell2['column_numbers']) < 2
            )
            or len(supercell2['row_numbers']) == 0
            or len(supercell2['column_numbers']) == 0
        ):
            suppression[supercell2_num] = True

    return [obj for idx, obj in enumerate(supercells) if not suppression[idx]]


def remove_supercell_overlap(supercell1, supercell2):
    """
    This function resolves overlap between supercells (supercells must be
    disjoint) by iteratively shrinking supercells by the fewest grid cells
    necessary to resolve the overlap.
    Example:
    If two supercells overlap at grid cell (R, C), and supercell #1 is less
    confident than supercell #2, we eliminate either row R from supercell #1
    or column C from supercell #1 by comparing the number of columns in row R
    versus the number of rows in column C. If the number of columns in row R
    is less than the number of rows in column C, we eliminate row R from
    supercell #1. This resolves the overlap by removing fewer grid cells from
    supercell #1 than if we eliminated column C from it.
    """
    common_rows = set(supercell1['row_numbers']).intersection(
        set(supercell2['row_numbers'])
    )
    common_columns = set(supercell1['column_numbers']).intersection(
        set(supercell2['column_numbers'])
    )

    # While the supercells have overlapping grid cells, continue shrinking the less-confident
    # supercell one row or one column at a time
    while len(common_rows) > 0 and len(common_columns) > 0:
        # Try to shrink the supercell as little as possible to remove the overlap;
        # if the supercell has fewer rows than columns, remove an overlapping column,
        # because this removes fewer grid cells from the supercell;
        # otherwise remove an overlapping row
        if len(supercell2['row_numbers']) < len(supercell2['column_numbers']):
            min_column = min(supercell2['column_numbers'])
            max_column = max(supercell2['column_numbers'])
            if max_column in common_columns:
                common_columns.remove(max_column)
                supercell2['column_numbers'].remove(max_column)
            elif min_column in common_columns:
                common_columns.remove(min_column)
                supercell2['column_numbers'].remove(min_column)
            else:
                supercell2['column_numbers'] = []
                common_columns = set()
        else:
            min_row = min(supercell2['row_numbers'])
            max_row = max(supercell2['row_numbers'])
            if max_row in common_rows:
                common_rows.remove(max_row)
                supercell2['row_numbers'].remove(max_row)
            elif min_row in common_rows:
                common_rows.remove(min_row)
                supercell2['row_numbers'].remove(min_row)
            else:
                supercell2['row_numbers'] = []
                common_rows = set()


def refine_rows(rows, threshold=0.5):
    """
    Apply operations to the detected rows, such as
    thresholding, NMS, and alignment.
    """

    rows = nms(
        rows,
        match_criteria="object2_overlap",
        match_threshold=threshold,
        keep_higher=True,
    )
    if len(rows) > 1:
        rows = sort_objects_top_to_bottom(rows)

    return rows


def refine_columns(columns, threshold=0.5):
    """
    Apply operations to the detected columns, such as
    thresholding, NMS, and alignment.
    """
    columns = nms(
        columns,
        match_criteria="object2_overlap",
        match_threshold=threshold,
        keep_higher=True,
    )
    if len(columns) > 1:
        columns = sort_objects_left_to_right(columns)

    return columns


def align_columns(columns, bbox):
    """
    For every column, align the top and bottom boundaries to the final
    table bounding box.
    """
    try:
        for column in columns:
            column['bbox'][1] = bbox[1]
            column['bbox'][3] = bbox[3]
    except Exception as err:
        print("Could not align columns: {}".format(err))
        pass

    return columns


def align_rows(rows, bbox):
    """
    For every row, align the left and right boundaries to the final
    table bounding box.
    """
    try:
        for row in rows:
            row['bbox'][0] = bbox[0]
            row['bbox'][2] = bbox[2]
    except Exception as err:
        print("Could not align rows: {}".format(err))
        pass

    return rows


def refine_table_structure(table_structure, class_thresholds):
    """
    Apply operations to the detected table structure objects such as
    thresholding, NMS, and alignment.
    """
    rows = table_structure["rows"]
    columns = table_structure['columns']
    spanning_cells = table_structure['spanning_cells']

    # Process spanning cells
    spanning_cells = apply_threshold(
        spanning_cells, class_thresholds["table spanning cell"]
    )

    # Align before NMS for spanning cells because alignment brings them into agreement
    # with rows and columns first; if spanning cells still overlap after this operation,
    # the threshold for NMS can basically be lowered to just above 0
    spanning_cells = align_supercells(spanning_cells, rows, columns)
    spanning_cells = nms_supercells(spanning_cells)

    table_structure['columns'] = columns
    table_structure['rows'] = rows
    table_structure['spanning_cells'] = spanning_cells

    return table_structure
