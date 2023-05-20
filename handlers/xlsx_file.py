""""""
import pandas as pd


from settings import data_dir, time_stamp


class XlsxBase:

    def create_table(self, data):
        pass

    def create_xlsx(self, data: dict[dict]):
        table, headers_lines, headers_columns = self.create_table(data)
        self.create_xlsx_file(table, headers_lines, headers_columns)

    @staticmethod
    def create_xlsx_file(table: list[list], line_index: list[dict], columns: list[str]):
        """"""
        path_to_file = data_dir / 'xlsx_files' / f'data_{time_stamp}.xlsx'

        df = pd.DataFrame(table, index=line_index, columns=columns)
        df.to_excel(path_to_file, sheet_name='Sheet1', startrow=0, startcol=0)


class XlsxFile(XlsxBase):

    def create_table(self, data: list[dict]):
        table = []
        headers_lines = []
        for exchanger in data:
            for currency in list(exchanger.values())[0]:
                row = list(currency.values())
                table.append(row)

                headers_lines.append(list(exchanger.keys())[0])
        headers_columns = list(list(data[0].values())[0][0].keys())
        return table, headers_lines, headers_columns


class XlsxFileOnlyCmc(XlsxBase):

    def create_table(self, data: dict[dict]):
        """"""
        table = []
        headers_lines = []
        for currency in data:
            row = list(data[currency].values())
            table.append(row)

            headers_lines.append(currency)

        headers_columns = list(list(data.values())[0].keys())
        return table, headers_lines, headers_columns

