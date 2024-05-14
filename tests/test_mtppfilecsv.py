import csv
from mtpp import MTPPData, MTPPFileCSV


INPUT_FILE_UTF8 = "tests/data/sampledata-utf8.csv"
INPUT_FILE_SJIS = "tests/data/sampledata-sjis.csv"
OUTPUT_FILE_UTF8 = "tests/data/sampledata-out-utf8.csv"
OUTPUT_FILE_SJIS = "tests/data/sampledata-out-sjis.csv"
ENCODING_UTF8 = "UTF-8"
ENCODING_SJIS = "Shift_JIS"
RECORDS = [
    {"都道府県": "鹿児島県", "カラム1": "119", "カラム2": "250"},
    {"都道府県": "徳島県", "カラム1": "193", "カラム2": "31"},
    {"都道府県": "大分県", "カラム1": "187", "カラム2": "206"},
    {"都道府県": "宮崎県", "カラム1": "162", "カラム2": "192"},
    {"都道府県": "愛媛県", "カラム1": "89", "カラム2": "236"},
    {"都道府県": "山口県", "カラム1": "94", "カラム2": "235"},
    {"都道府県": "徳島県", "カラム1": "73", "カラム2": "86"},
    {"都道府県": "神奈川県", "カラム1": "207", "カラム2": "103"},
    {"都道府県": "熊本県", "カラム1": "50", "カラム2": "91"},
    {"都道府県": "山梨県", "カラム1": "198", "カラム2": "20"},
    {"都道府県": "富山県", "カラム1": "170", "カラム2": "17"},
    {"都道府県": "高知県", "カラム1": "96", "カラム2": "102"},
    {"都道府県": "鳥取県", "カラム1": "89", "カラム2": "239"},
    {"都道府県": "岐阜県", "カラム1": "27", "カラム2": "198"},
    {"都道府県": "東京都", "カラム1": "175", "カラム2": "201"},
    {"都道府県": "福島県", "カラム1": "136", "カラム2": "49"},
    {"都道府県": "神奈川県", "カラム1": "191", "カラム2": "147"},
    {"都道府県": "宮崎県", "カラム1": "180", "カラム2": "33"},
    {"都道府県": "静岡県", "カラム1": "236", "カラム2": "201"},
    {"都道府県": "滋賀県", "カラム1": "249", "カラム2": "59"},
    {"都道府県": "岡山県", "カラム1": "8", "カラム2": "181"},
    {"都道府県": "静岡県", "カラム1": "11", "カラム2": "188"},
    {"都道府県": "和歌山県", "カラム1": "40", "カラム2": "89"},
    {"都道府県": "千葉県", "カラム1": "252", "カラム2": "106"},
    {"都道府県": "埼玉県", "カラム1": "2", "カラム2": "65"},
]


class TestMTPPFileCSV:
    def test_csv_instance_utf8(self):
        target = MTPPFileCSV.read(INPUT_FILE_UTF8, ENCODING_UTF8)
        assert isinstance(target, MTPPData)

    def test_csv_instance_sjis(self):
        target = MTPPFileCSV.read(INPUT_FILE_SJIS, ENCODING_SJIS)
        assert isinstance(target, MTPPData)

    def test_csv_read_utf8(self):
        target = MTPPFileCSV.read(INPUT_FILE_UTF8, ENCODING_UTF8)
        assert target == RECORDS

    def test_csv_read_sjis(self):
        target = MTPPFileCSV.read(INPUT_FILE_SJIS, ENCODING_SJIS)
        assert target == RECORDS

    def test_csv_write_utf8(self):
        data = MTPPData(RECORDS)
        MTPPFileCSV.write(data, OUTPUT_FILE_UTF8, ENCODING_UTF8)
        with open(OUTPUT_FILE_UTF8, encoding=ENCODING_UTF8) as f:
            reader = csv.DictReader(f)
            records = list(reader)
        assert records == RECORDS

    def test_csv_write_sjis(self):
        data = MTPPData(RECORDS)
        MTPPFileCSV.write(data, OUTPUT_FILE_SJIS, ENCODING_SJIS)
        with open(OUTPUT_FILE_SJIS, encoding=ENCODING_SJIS) as f:
            reader = csv.DictReader(f)
            records = list(reader)
        assert records == RECORDS