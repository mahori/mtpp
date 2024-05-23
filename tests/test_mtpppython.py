from collections import defaultdict

from mtpp import MTPPData, MTPPPython

from .constant import PYTHON_BEFORE_CALL, PYTHON_AFTER_CALL


def python_call_function(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    prefectures = defaultdict(list)

    for row in rows:
        prefecture = row["都道府県"]
        prefectures[prefecture].append(row)

    for prefecture, values in prefectures.items():
        index = 0
        prev = 0
        for index, value in enumerate(values):
            if prev > 100:
                break
            prev = int(value["カラム1"])
        else:
            index += 1
        del values[index:]

    rows = [row for rows in prefectures.values() for row in rows]

    return rows


class TestMTPPPython:
    def test_instance(self):
        target = MTPPPython()
        assert isinstance(target, MTPPPython)

    def test_call(self):
        target = MTPPPython()
        before = MTPPData(PYTHON_BEFORE_CALL)
        after = target(before, python_call_function)
        assert after == PYTHON_AFTER_CALL
