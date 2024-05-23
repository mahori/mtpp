from typing import Union

from .core import MTPPCall, MTPPData


#
# MTPPPython クラス
#


class MTPPPython(MTPPCall):
    """
    Pythonスクリプトで処理をするためのクラス

    実際の処理はクロージャ(関数，メソッド，ラムダ関数)をつくりそれを__call__メソッドに渡すことで行う
    """

    def __call__(self, data: MTPPData, call_function, /, *args) -> MTPPData:
        """
        Pythonスクリプトで処理をするメソッド

        Parameters:
        call_function (クロージャ): 実際に処理を行うクロージャ
        data (MTPPData): 処理のためのデータ
        """
        if not isinstance(data, MTPPData):
            raise TypeError

        data = data.rows

        if isinstance(call_function, list):
            for function in call_function:
                if isinstance(function, tuple):
                    function, *args = function  # type: ignore
                    data = function(data, *args)
                else:
                    data = function(data)
        else:
            data = call_function(data, *args)

        return MTPPData(data)


#
# ヘルパー関数
#


def index_to_threshold(rows: list[dict[str, str]], column: str, threshold: Union[int, float]) -> int:
    """
    閾値までをスキャンして返す
      スキャンしたあと閾値を超えたインデックスを返す
      ループを最後まで行った(閾値を超えなかった)ときは最後のインデックス+1を返す
      Python処理用の関数なのでMTPPPythonクラスの__call__メソッドに渡されるデータ型(list[dict[str, str]])を受け取る

    Parameters:
    rows (list[dict[str, str]]) 対象データ
    column (str): 対象カラム名
    threshold (T): 閾値
    """
    index = 0

    for index, row in enumerate(rows):
        current: Union[int, float]

        if isinstance(threshold, int):
            current = int(row[column])
        elif isinstance(threshold, float):
            current = float(row[column])
        else:
            raise NotImplementedError

        if current > threshold:
            break
    else:
        index += 1

    return index


def index_on_threshold(rows: list[dict[str, str]], column: str, threshold: Union[int, float]) -> int:
    """
    閾値までをスキャンして返す
      閾値を超えたところのインデックスは採用する
      スキャンしたあと採用しない最初のインデックスを返す
      ループを最後まで行った(閾値を超えなかった)ときは最後のインデックス+1を返す
      Python処理用の関数なのでMTPPPythonクラスの__call__メソッドに渡されるデータ型(list[dict[str, str]])を受け取る

    Parameters:
    rows (list[dict[str, str]]) 対象データ
    column (str): 対象カラム名
    threshold (T): 閾値
    """
    prev: Union[int, float]

    if isinstance(threshold, int):
        prev = 0
    elif isinstance(threshold, float):
        prev = 0.0
    else:
        raise NotImplementedError

    index = 0

    for index, row in enumerate(rows):
        if prev > threshold:
            break

        if isinstance(threshold, int):
            prev = int(row[column])
        elif isinstance(threshold, float):
            prev = float(row[column])
        else:
            raise NotImplementedError
    else:
        index += 1

    return index
