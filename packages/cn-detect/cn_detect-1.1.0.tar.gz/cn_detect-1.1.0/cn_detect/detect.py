import re
import pandas as pd
from cn_detect.config import CHINESE_FAMILY_NAME


def read_txt_file(filename_path: str):
    if not filename_path.endswith('.txt'):
        raise ValueError('The filename file must be a .txt file.')
    try:
        with open(filename_path, 'r', encoding='utf-8') as f:
            data = [line.strip() for line in f]
        return data
    except FileNotFoundError:
        print(f"File not found: {filename_path}")
        return []
    except Exception as e:
        print(f"Error reading file {filename_path}: {e}")
        return []

class ChineseNameDetect:
    def __init__(self, family_name_file: str = None):
        """
        Initialize ChineseNameDetect class with a file containing Chinese family names.
        :param family_name_file: Path to the file containing Chinese family names.
        """
        if family_name_file:
            self.full_names = read_txt_file(family_name_file)
        else:
            self.full_names = CHINESE_FAMILY_NAME

    @staticmethod
    def detect_chinese_word(data: str) -> bool:
        """
        Detect if the given string contains Chinese characters.
        :param data: The string to check.
        :return: True if Chinese characters are found, False otherwise.
        """
        chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
        if isinstance(data, str):
            return bool(chinese_pattern.search(data))
        return False

    def detect_family_name(self, data: str) -> bool:
        """
        Detect if the given string contains a known Chinese family name.
        :param data: The string to check.
        :return: True if a family name is found, False otherwise.
        """
        if not isinstance(data, str):
            return False

        split_name = data.split()
        for name in split_name:
            if name.lower() in self.full_names and name.lower() != 'nan':
                return True
        return False

    def detect_each_row_by_column(self, row: pd.Series, column: str) -> str:
        """
        Detect Chinese characters or family names in a specified column of a row.
        :param row: The DataFrame row to check.
        :param column: The column name to check.
        :return: The original value if Chinese characters or family names are detected, else an empty string.
        """
        data = row[column]
        if self.detect_chinese_word(data) or self.detect_family_name(data):
            return data
        return ''

    def recognize_excel_by_column(self, excel_file_path: str, column: str):
        """
        Process an Excel file to detect Chinese characters or family names in a specified column.
        :param excel_file_path: Path to the Excel file.
        :param column: The column name to check.
        """
        try:
            df = pd.read_excel(excel_file_path)
            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found in the Excel file.")

            df['Chinese'] = df.apply(lambda row: self.detect_each_row_by_column(row, column), axis=1)
            cn_excel_file_path = excel_file_path.replace('.xlsx', '_cn.xlsx')
            df.to_excel(cn_excel_file_path, index=False)
            print(f"The Excel file has been saved to {cn_excel_file_path}")
        except FileNotFoundError:
            print(f"Excel file not found: {excel_file_path}")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error processing Excel file {excel_file_path}: {e}")

