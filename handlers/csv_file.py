""""""
import csv


from settings import data_dir, time_stamp


class CsvBase:
    """"""

    def create_csv_file(self, data: dict[dict]):
        """"""
        csv_table = self.create_table(data)
        self.write_csv_file(csv_table)


    @staticmethod
    def write_csv_file(csv_table: list[list], delimiter: str = ','):
        """
        Input: Nested list csv_table and a string file_name
        Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
        """
        file_name = data_dir / 'csv_files' / f'data_{time_stamp}.csv'

        with open(file_name, 'w', newline='', encoding='UTF-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)
            for row in csv_table:
                csv_writer.writerow(row)


class CsvFile(CsvBase):
    """"""

    @staticmethod
    def create_table(data: list[dict]) -> list[list]:
        """"""
        table = []
        for exchanger in data:
            for currency in list(exchanger.values())[0]:
                row = list(currency.values())
                table.append(row)

        first_line = list(list(data[0].values())[0][0].keys())
        table.insert(0, first_line)
        return table


class CsvFileOnlyCmc(CsvBase):
    """"""

    @staticmethod
    def create_table(data: dict[dict]) -> list[list]:
        """"""
        table = []
        for currency in data:
            row = list(data[currency].values())
            table.append(row)

        first_line = list(list(data.values())[0].keys())
        table.insert(0, first_line)
        return table
