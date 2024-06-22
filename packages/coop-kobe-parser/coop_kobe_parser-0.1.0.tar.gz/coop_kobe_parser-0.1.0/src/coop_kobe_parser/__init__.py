import json
from pandas import read_csv, DataFrame, Series
from pandas.errors import EmptyDataError, ParserError

from coop_kobe_parser.logger import init_logger
from coop_kobe_parser.parsers import ProductParser, SummaryParser


def main():
    """
    動作確認用
    CoopKobeParser インスタンスを作成し、CSV ファイルを解析します。
    """

    # パーサーのインスタンスを作成
    parser = CoopKobeParser()

    # 解析する CSV ファイルのパス
    csv_path = "demo/demo.csv"

    # CSV ファイルを解析
    data = parser.parse(csv_path)
    print(json.dumps(data, indent=4, ensure_ascii=False))


class CoopKobeParser:
    def __init__(self):
        """
        CoopKobeParser クラスの初期化。
        """
        self.logger = init_logger()

    def parse(self, csv_path: str) -> dict:
        """
        CSV ファイルを解析し、種別ごとに分離した上で取得する

        Parameters:
        csv_path (str): 解析する CSV ファイルのパス

        Returns:
        dict: パース結果
        """
        # CSV ファイルを読み込み
        df = self._load_csv(csv_path)

        # 商品一覧と支払情報のデータフレームに分ける
        df_products, df_summary = self._divide_df(df)

        # 商品一覧をパースして配列化する
        products = ProductParser(df_products).parse()

        # 支払情報をパースする
        summary = SummaryParser(df_summary).parse()

        return {"products": products, "summary": summary}

    def _load_csv(self, path: str) -> DataFrame:
        """
        CSV ファイルを読み込み、データフレームを返却する

        Parameters:
        path (str): 読み込む CSV ファイルのパス

        Returns:
        DataFrame: CSV ファイルから読み込んだデータフレーム
        """
        try:
            # CSV ファイルを読み込み
            df = read_csv(path, dtype=str)
            return df
        except FileNotFoundError:
            self.logger.error(f"ファイル {path} が見つかりませんでした。")
        except (EmptyDataError, ParserError):
            self.logger.error(f"ファイル {path} の読み込み中にエラーが発生しました。")
            return None

    def _divide_df(self, df: DataFrame) -> tuple[Series, Series]:
        """
        商品一覧と支払情報のデータフレームに分ける

        Parameters:
        df (DataFrame): CSV ファイルから読み込んだデータフレーム

        Returns:
        tuple[DataFrame, DataFrame]: 商品一覧のデータフレームと支払情報のデータフレームのタプル
        """

        # 品番が存在するかどうかを確認
        if "品番" not in df.columns:
            raise ValueError("品番列がデータフレームに存在しません。")

        # 商品一覧のデータフレームを取得 (品番がNaNでない)
        df_products = df[df["品番"].notna()]

        # 支払情報のデータフレームを取得 (品番がNaN)
        df_summary = df[df["品番"].isna()]

        # 商品一覧と支払情報のデータフレームが空でないことを確認
        if df_products.empty or df_summary.empty:
            raise ValueError("商品一覧または支払情報のデータフレームが空です。")

        return df_products, df_summary
