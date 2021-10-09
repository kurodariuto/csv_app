from csv_opretion import CsvReader
from checker import MinMaxChecker
from config import CsvConfig

MinMaxChecker = MinMaxChecker()
CsvReader = CsvReader()
CsvConfig = CsvConfig() # CSVを操作するために必要な情報を持つクラスのインスタンス

# 最小値か最大化をチェック（大文字のバリデーションもしている）
MinMaxChecker.check = CsvConfig.MAX_OR_MIN
MinMaxChecker.check

# ディレクトリや、列や行の指定
CsvReader.directory = CsvConfig.DIRECTORY
CsvReader.start_set_row_count = CsvConfig.START_SET_ROW_COUNT
CsvReader.end_set_row_count = CsvConfig.END_SET_ROW_COUNT
CsvReader.set_column_count = CsvConfig.SET_COLUMN_COUNT
CsvReader.directory
CsvReader.start_set_row_count
CsvReader.end_set_row_count
CsvReader.set_column_count

# ディレクトリや列や行の指定を元に、CSVを読み込む
CsvReader.read_range(
    CsvConfig.MAX_OR_MIN,
    CsvReader.directory,
    CsvReader.start_set_row_count,
    CsvReader.end_set_row_count,
    CsvReader.set_column_count
)










# directory = "2021.9.13_2021.9.16"
# file_path_list = os.listdir(path=directory)
# start_set_row_count = 60
# end_set_row_count = 90
# set_column_count = 2
# set_column_count = 1
#
# max_or_min = "MAX"
# path = "./" + max_or_min + "/" + directory
# os.mkdir(path)

# for file in file_path_list:
#     print("ファイル名")
#     print(file)
#     root_ext_pair = os.path.splitext(file)
#     if (root_ext_pair[1] == ".xlsx"):
#         print(".xlsxのため処理をスキップ")
#         print(root_ext_pair)
#         continue
#     with open( directory + "/" + file, "r", encoding="shift-jis") as f:
#         apend_list = []
#         row_count = 0
#         reader = csv.reader(f)
#         for line in reader:
#             row_count += 1
#             if(row_count >= 60 and row_count <= 80):
#                 print(row_count)
#                 print(line[0])
#                 apend_list.append(line[0])
#             elif (row_count > 80):
#                 print("break")
#                 break
#         # ログ
#         max_or_min_list = max(apend_list)
#         print(max_or_min_list)
#         with open(path + "/" + max_or_min + file, "w") as f:
#             writer = csv.writer(f)
#             writer.writerow(["MAX", max_or_min_list])
#             # writer.writerow(['a', 'b', 'c'])





