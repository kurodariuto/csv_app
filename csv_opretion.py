import os
import csv
from config import CsvConfig
from checker import MinMaxChecker

# CSVを操作するために必要な情報を持つクラスのインスタンス
CsvConfig = CsvConfig()

class CsvReader:
    @property
    def directory(self):
        """
        Returns
        ------
        .__start_set_row_count：str
        """
        return self.__directory

    @directory.setter
    def directory(self, directory: str):
        """
        Parameters
        ----------
         directory : str
            CSVを格納したディレクトリ名
        """
        if type(directory) is not str:
            raise TypeError("directory must be str")
        self.__directory = directory

    @property
    def start_set_row_count(self):
        """"
        Returns
        -------
        .__start_set_row_count:int
        """
        return self.__start_set_row_count

    @start_set_row_count.setter
    def start_set_row_count(self, start_set_row_count:int):
        """
        Parameters
        ----------
        start_set_row_coun :int
            行範囲の最初の行番号
        """
        if type(start_set_row_count) is not int:
            raise TypeError("start_set_row_count must be int")
        self.__start_set_row_count = start_set_row_count

    @property
    def end_set_row_count(self):
        """
        ----------
        Returns
        .__end_set_row_count :int
        """
        return self.__end_set_row_count

    @end_set_row_count.setter
    def end_set_row_count(self, end_set_row_count:int):
        """
        Parameters
        ----------
         end_set_row_count:int
            行範囲の最後の行番号
        """
        if type(end_set_row_count) is not int:
            raise TypeError("start_set_row_count must be int")
        self.__end_set_row_count = end_set_row_count

    @property
    def set_column_count(self):
        """
        Returns
        ----------
        .__set_column_count:int
        """
        return self.__set_column_count

    @set_column_count.setter
    def set_column_count(self, set_column_count:int):
        """
        Parameter
        ----------
        set_column_count:int
            列番号
        """
        if type(set_column_count) is not int:
            raise TypeError("set_column_count must be int")
        self.__set_column_count = set_column_count

    def read_range(self, min_or_max, directory, start_set_row_count, end_set_row_count, set_column_count):
        """
        Method
        ----------
        read_range
            指定された列と行範囲で、CSVを読み込む

        Parameter
        ----------
        min_or_max：int
            MINか、MAX：str

        directory：str
            ディレクト名

        start_set_row_count：int
            範囲の最初の行番号

        end_set_row_count：int
            範囲の最後の行番号

        set_column_count：int
            列番号
        """
        file_path_list = os.listdir(path=directory)
        global path
        global reader_list
        path = "./" + min_or_max + directory
        os.mkdir(path)
        for file in file_path_list:

            # ログ
            print("ファイル名")
            print(file)
            root_ext_pair = os.path.splitext(file)
            if (root_ext_pair[1] == ".xlsx"):

                # ログ
                print(".xlsxのため処理をスキップ")
                print(root_ext_pair)
                continue
            with open(directory + "/" + file, "r", encoding="shift-jis") as f:
                row_count = 0
                reader = csv.reader(f)
                for line in reader:
                    row_count += 1
                    if (row_count >= start_set_row_count and row_count <= end_set_row_count):

                        # ログ
                        print(row_count)
                        print(line[set_column_count])
                        reader_list = []
                        reader_list.append(line[set_column_count])
                    elif (row_count > end_set_row_count):
                        print("break")
                        break

                # 読み込んだCSVを書き込む
                csv_writer = CsvWriter()
                csv_writer.write(reader_list, CsvConfig.MAX_OR_MIN)

class CsvWriter:
    def write(self, reader_list, min_or_max):
        """
        Method
        ----------
        write
            指定した範囲内の最小値または、最大値を書き込む

        Parameter
        ----------
        reader_list：list
            指定した行範囲内の、CSVのリスト

        min_or_max：str
            MINまたは、MAX
        """
        for file in reader_list:
            if(min_or_max == "MIN"):
                min_or_max_list = max(reader_list)
                print(min_or_max_list)
            elif (min_or_max == "MAX"):
                min_or_max_list = min(reader_list)
                print(min_or_max_list)
            with open(path + "/" + min_or_max + file, "w") as f:
                writer = csv.writer(f)
                writer.writerow([min_or_max, min_or_max_list])

if __name__ == "__main__":
    MinMaxChecker()

if __name__ == "__main__":
    CsvReader()