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