""""""
import pandas as pd


from settings import base_dir, time_stamp


def create_table(data: dict[dict]):
    table = []
    headers_lines = []
    for currency in data:
        row = list(data[currency].values())
        table.append(row)

        headers_lines.append(currency)

    headers_columns = list(list(data.values())[0].keys())
    return table, headers_lines, headers_columns


def create_xls_file(table: list[list], line_index: list[dict], columns: list[str]):
    """"""
    path_to_file = base_dir / 'xlsx_files' / f'data_{time_stamp}.xlsx'

    df = pd.DataFrame(table, index=line_index, columns=columns)
    df.to_excel(path_to_file, sheet_name='Sheet1', startrow=0, startcol=0)


def create_xlsx_file(data: dict[dict]):
    table, headers_lines, headers_columns = create_table(data)
    create_xls_file(table, headers_lines, headers_columns)
