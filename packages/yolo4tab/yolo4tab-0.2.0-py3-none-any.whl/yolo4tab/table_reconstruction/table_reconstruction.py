from typing import Dict, List

from fitz import Rect

from ..const import BorderFormat, HorizontalAlign, OutputFormat, VerticalAlign


class TableReconstruction:
    def __init__(self) -> None:
        pass

    def process(
        self,
        table_structure: Dict,
        table_values: Dict,
        output_formats: List[OutputFormat] = [
            OutputFormat.HTML,
            OutputFormat.LATEX,
            OutputFormat.CSV,
        ],
        border_format: BorderFormat = BorderFormat.FULL_BORDER,
        vertical_align: VerticalAlign = VerticalAlign.MIDDLE,
        horizontal_align: HorizontalAlign = HorizontalAlign.LEFT,
    ) -> Dict:
        """Process table components and values to reconstruct table

        Args:
            table_structure (Dict): Table components detected by table structure recognition module
            table_values (Dict): Table values detected by text extraction module
            output_format (List[OutputFormat]): List of output formats to reconstruct table
            border_format (BorderFormat, optional): Border format of the table. Defaults to BorderFormat.FULL_LINE.
            vertical_align (VerticalAlign, optional): Vertical align of the table. Defaults to VerticalAlign.MIDDLE.
            horizontal_align (HorizontalAlign, optional): Horizontal align of the table. Defaults to HorizontalAlign.LEFT.

        Returns:
            Dict: Dictionary of outputs and table cells.
        """
        ## Verify output formats, border format, vertical align, horizontal align
        all_output_formats = [i for i in OutputFormat]
        all_border_formats = [i for i in BorderFormat]
        all_vertical_aligns = [i for i in VerticalAlign]
        all_horizontal_aligns = [i for i in HorizontalAlign]

        assert all(
            output_format in all_output_formats for output_format in output_formats
        ), f"Invalid output format: {output_formats}"
        assert (
            border_format in all_border_formats
        ), f"Invalid border format: {border_format}"
        assert (
            vertical_align in all_vertical_aligns
        ), f"Invalid vertical align: {vertical_align}"
        assert (
            horizontal_align in all_horizontal_aligns
        ), f"Invalid horizontal align: {horizontal_align}"

        ## Get cells from table structure
        table_cells = table_structure["cells"]
        num_rows = table_structure["num_rows"]
        num_columns = table_structure["num_columns"]
        table_cells = self._fill_values(table_cells, table_values)
        table_cells = self._group_values(table_cells)

        ## Format output
        output = {}
        for output_format in output_formats:
            output[output_format] = self._format_output(
                table_cells,
                num_rows,
                num_columns,
                output_format,
                border_format,
                vertical_align,
                horizontal_align,
            )

        return {
            "outputs": output,
            "table_cells": table_cells,
            "num_rows": num_rows,
            "num_cols": num_columns,
        }

    def _fill_values(
        self, table_cells: List[Dict], table_values: List[Dict]
    ) -> List[Dict]:
        """Fill values from TE module into table structure from TSR module

        Args:
            table_cells (List[Dict]): List of cells in table. Cells are represented by dictionary with keys: bbox, column_nums, row_nums
            table_values (List[Dict]): List of values detected by text extraction module. Values are represented by dictionary with keys: bbox, text, center

        Returns:
            List[Dict]: List of cells in table with values filled. Cells are represented by dictionary with keys: bbox, column_nums, row_nums, values
        """
        sorted_instances = sorted(
            table_values, key=lambda x: (x['center'][0], x['center'][1])
        )
        for cell in table_cells:
            cell['values'], remaining_values = [], []

            for value in sorted_instances:
                if Rect(cell['bbox']).contains(value['center']):
                    cell['values'].append(value)
                else:
                    remaining_values.append(value)
            sorted_instances = remaining_values.copy()
        return table_cells

    def _group_values(self, table_cells: List[Dict]) -> List[Dict]:
        """Group values in the same cell into a single cell content

        Args:
            table (List[Dict]): table structure with values filled (not merged yet). Format:
                [
                    {
                        'bbox': [x1, y1, x2, y2],
                        'column_nums': [column_num1, column_num2, ...],
                        'row_nums': [row_num1, row_num2, ...],
                        'values': [
                            {
                                'bbox': [x1, y1, x2, y2],
                                'text': 'value',
                                'center': [x, y],
                            },
                            ...
                        ],
                    },
                    ...
                ]
            merge_dist (int, optional): Maximum distance between two values to be merged. Defaults to 10.

        Returns:
            List[Dict]: table structure with values grouped. Format:
                [
                    {
                        'bbox': [x1, y1, x2, y2],
                        'column_nums': [column_num1, column_num2, ...],
                        'row_nums': [row_num1, row_num2, ...],
                        'content': 'cell content',
                    },
                    ...
                ]
        """

        for cell in table_cells:
            if len(cell["values"]) == 0 or len(cell["values"]) == 1:
                cell["content"] = (
                    cell["values"][0]['text'] if len(cell["values"]) == 1 else ""
                )
                cell.pop("values", None)
                continue
            sorted_values = sorted(
                cell["values"], key=lambda x: (x['center'][1], x['center'][0])
            )

            line = 1
            pre_value = sorted_values[0]
            pre_value["line"] = line

            grouped_values = [pre_value]

            for value in sorted_values[1:]:
                if (
                    value["bbox"][1] < pre_value["center"][1]
                    and value["bbox"][3] > pre_value["center"][1]
                ):
                    value["line"] = line
                else:
                    line += 1
                    value["line"] = line
                    pre_value = value
                grouped_values.append(value)

            grouped_values = sorted(
                grouped_values, key=lambda x: (x["line"], x["center"][0])
            )

            pre_line = 1
            cell["content"] = grouped_values[0]["text"]
            for value in grouped_values[1:]:
                if value["line"] == pre_line:
                    cell["content"] += f" {value['text']}"
                else:
                    cell["content"] += f"\n{value['text']}"
                pre_line = value['line']

            cell.pop("values", None)
        return table_cells

    def _format_output(
        self,
        table_cells: List[Dict],
        num_rows: int,
        num_columns: int,
        output_format: OutputFormat,
        border_format: BorderFormat,
        vertical_align: VerticalAlign,
        horizontal_align: HorizontalAlign,
    ) -> str:
        """Format table to output format

        Args:
            table_cells (List[Dict]): table structure with values grouped after filling and grouping values of eachs cells.
            num_rows (int): Number of rows in table
            num_columns (int): Number of columns in table
            output_format (OutputFormat): Output format to convert table to
            border_format (BorderFormat): Border format of the table
            vertical_align (VerticalAlign): Vertical align of the table
            horizontal_align (HorizontalAlign): Horizontal align of the table

        Returns:
            str: Table content in output format
        """
        if output_format == OutputFormat.CSV:
            return self._to_csv(table_cells, num_rows, num_columns)
        elif output_format == OutputFormat.HTML:
            return self._to_html(
                table_cells,
                num_rows,
                num_columns,
                border_format,
                vertical_align,
                horizontal_align,
            )
        elif output_format == OutputFormat.LATEX:
            return self._to_latex(
                table_cells,
                num_rows,
                num_columns,
                border_format,
                vertical_align,
                horizontal_align,
            )

    def _to_csv(self, table_cells: List[Dict], num_rows: int, num_columns: int) -> str:
        """Convert table to csv format

        Args:
            table_cells (List[Dict]): table structure with values grouped after filling and grouping values of eachs cells.
            num_rows (int): number of rows in table
            num_columns (int): number of columns in table

        Returns:
            str: CSV string of table
        """
        ## Create an empty matrix
        output = [["" for _ in range(num_columns)] for _ in range(num_rows)]

        for cell in table_cells:
            row_num = cell["row_nums"][0]
            column_num = cell["column_nums"][0]
            content = cell["content"]
            if (
                content.find(",") != -1
                or content.find('\n') != -1
                or content.find('"') != -1
            ):
                content = content.replace("\n", "\\n")
                content = content.replace('"', "''")
                content = f'"{content}"'
            output[row_num][column_num] = content

        ## Convert to csv format with each row is a line, each cell is separated by comma
        output = [",".join(row) for row in output]
        output = "\n".join(output)
        return output

    def _to_html(
        self,
        table_cells: List[Dict],
        num_rows: int,
        num_columns: int,
        border_format: BorderFormat,
        vertical_align: VerticalAlign,
        horizontal_align: HorizontalAlign,
    ) -> str:
        """Convert table to html format

        Args:
            table_cells (List[Dict]): table structure with values grouped after filling and grouping values of eachs cells.
            num_rows (int): number of rows in table
            num_columns (int): number of columns in table
            border_format (BorderFormat): Border format of the table
            vertical_align (VerticalAlign): Vertical align of the table
            horizontal_align (HorizontalAlign): Horizontal align of the table

        Returns:
            str: HTML code of table
        """

        ## Step 1: Create HTML table
        i_row, i_col = 0, 0
        script_table = ""

        while i_row < num_rows:
            i_col = 0
            text_row = ""
            while i_col < num_columns:
                text_cell = ""
                for cell in table_cells:
                    # coors here mean index (row, col) in table
                    col_nums = cell['column_nums']
                    row_nums = cell['row_nums']

                    # check if it is the last cell in the row (i_row)
                    if (col_nums[0] == i_col) and (row_nums[0] == i_row):
                        rowspan = len(row_nums)
                        colspan = len(col_nums)

                        content = cell["content"]
                        content = (
                            content.replace("<", "&lt;")
                            .replace(">", "&gt;")
                            .replace("&", "&amp;")
                        )
                        content = content.replace("\n", "<br>")

                        text_cell = "<td rowspan='{}', colspan='{}'>{}</td>".format(
                            str(rowspan), str(colspan), content
                        )
                text_row += text_cell
                i_col += 1

            text_row = "<tr>{}</tr>".format(text_row)
            script_table += text_row
            i_row += 1

        script_table = "<table>{}</table>".format(script_table)

        script_table = (
            script_table.replace("\"http", "'http")
            .replace("MathML\"", "MathML'")
            .replace("\"inline\"", "'inline'")
        )

        ## Step 2: Add style to HTML table
        ### Border format
        border_map = {
            BorderFormat.FULL_BORDER: "table, td {border-collapse: collapse; border: 1px solid black;}",
            BorderFormat.NO_BORDER: "table {border-collapse: collapse;}",
            BorderFormat.HOR_BORDER: "table {border-collapse: collapse;} td {border-top: 1px solid black; border-bottom: 1px solid black;}",
            BorderFormat.VER_BORDER: "table {border-collapse: collapse;} td {border-left: 1px solid black; border-right: 1px solid black;}",
            BorderFormat.INNER_BORDER: "table {border-collapse: collapse; border-style: hidden;} td {border: 1px solid black;}",
            BorderFormat.OUTER_BORDER: "table {border-collapse: collapse; border: 1px solid black;} td {border: none;}",
        }

        border = border_map[border_format]
        ### Align format
        align = (
            f"td {{text-align: {horizontal_align}; vertical-align: {vertical_align};}}"
        )

        style = f"<style>{border} {align}</style>"

        html_code = f"{style} {script_table}"

        return html_code

    def _to_latex(
        self,
        table_cells: List[Dict],
        num_rows: int,
        num_columns: int,
        border_format: BorderFormat,
        vertical_align: VerticalAlign,
        horizontal_align: HorizontalAlign,
    ) -> str:
        """Convert table to latex format

        Args:
            table_cells (List[Dict]): table structure with values grouped after filling and grouping values of eachs cells.
            num_rows (int): number of rows in table
            num_columns (int): number of columns in table
            border_format (BorderFormat): Border format of the table
            vertical_align (VerticalAlign): Vertical align of the table
            horizontal_align (HorizontalAlign): Horizontal align of the table

        Returns:
            str: Latex code of table
        """
        v_align_map = {
            VerticalAlign.TOP: "h",
            VerticalAlign.MIDDLE: "m",
            VerticalAlign.BOTTOM: "f",
        }
        h_align_map = {
            HorizontalAlign.LEFT: "l",
            HorizontalAlign.CENTER: "c",
            HorizontalAlign.RIGHT: "r",
        }

        ## Step 1: Create Latex table
        structure = ""
        for cell in table_cells:
            r = cell["row_nums"][0] + 1
            c = cell["column_nums"][0] + 1
            n_c = len(cell['column_nums'])
            n_r = len(cell['row_nums'])
            structure += (
                "cell{"
                + str(r)
                + "}{"
                + str(c)
                + "}= {c="
                + str(n_c)
                + ", r="
                + str(n_r)
                + "}{"
                + h_align_map[horizontal_align]
                + ","
                + v_align_map[vertical_align]
                + "},"
            )

        table_value = ""
        i_row, i_col = 0, 0
        while i_row < num_rows:
            i_col = 0
            text_row = ""
            while i_col < num_columns:
                text_cell = ""
                for cell in table_cells:
                    col_nums = cell['column_nums']
                    row_nums = cell['row_nums']
                    if (col_nums[0] == i_col) and (row_nums[0] == i_row):
                        content = cell["content"]
                        content = (
                            content.replace("\\", "$\\backslash$")
                            .replace("#", "\\#")
                            .replace("$", "\\$")
                            .replace("%", "\\%")
                            .replace("&", "\\&")
                            .replace("_", "\\_")
                            .replace("~", "\\textasciitilde{}")
                            .replace("^", "\\textasciicircum{}")
                            .replace("}", "\\}")
                            .replace("{", "\\{")
                        )
                        content = content.replace("\n", "\\\\")
                        text_cell = "{" + content + "}"
                text_row += text_cell + "&"
                i_col += 1

            text_row = text_row[:-1]
            text_row = f"{text_row}\\\\"
            table_value += text_row
            i_row += 1

        ## Border format
        border_map = {
            BorderFormat.FULL_BORDER: "hlines, vlines, ",
            BorderFormat.NO_BORDER: "",
            BorderFormat.HOR_BORDER: "hlines, ",
            BorderFormat.VER_BORDER: "vlines, ",
            BorderFormat.INNER_BORDER: "hlines, vlines, hline{1,Z} = {0pt}, vline{1,Z} = {0pt}, ",
            BorderFormat.OUTER_BORDER: "hline{1,Z} = {1pt,solid}, vline{1,Z} = {1pt,solid}, ",
        }
        border = border_map[border_format]

        script_table = (
            "\\begin{tblr}{" + border + structure + "} " + table_value + "\n\\end{tblr}"
        )

        doc_script = (
            "\\documentclass{article}\n\\usepackage{geometry}\n\\geometry{a4paper,margin=2mm}\n\\usepackage{tabularray}\n\\usepackage[utf8]{vietnam}\n\\begin{document}\\begin{center}\n"
            + script_table
            + "\n\\end{center}\n\\end{document}"
        )

        return doc_script
