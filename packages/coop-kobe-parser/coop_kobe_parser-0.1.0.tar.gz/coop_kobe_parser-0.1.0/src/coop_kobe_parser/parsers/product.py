from pandas import Series

from coop_kobe_parser.logger import init_logger


class ProductParser:
    """
    商品情報をパースするクラス。

    Attributes:
        df (Series): 商品情報のデータフレーム。
    """

    def __init__(self, df: Series):
        """
        ProductParser クラスの初期化。

        Args:
            df (Series): 商品情報のデータフレーム。
        """
        self.df = df
        self.logger = init_logger()

    def _rename_columns(self):
        """
        データフレームのカラム名を変更する。
        """
        try:
            self.df = self.df.rename(
                columns={
                    "商品名": "name",
                    "本体価格": "price",
                    "数量": "amount",
                    "小計": "subtotal",
                }
            )
        except Exception as e:
            self.logger.error(f"カラム名の変更に失敗しました: {e}")

    def _remove_commas_from_numbers(self):
        """
        数値のカンマ区切りを削除する。
        """
        try:
            for col in ["price", "subtotal"]:
                self.df[col] = self.df[col].str.replace(",", "")
        except Exception as e:
            self.logger.error(f"数値のカンマ区切りの削除に失敗しました: {e}")

    def _convert_to_int(self):
        """
        'price', 'amount', 'subtotal' のカラムを int 型に変換する。
        """
        try:
            for col in ["price", "amount", "subtotal"]:
                self.df[col] = self.df[col].astype(int)
        except Exception as e:
            self.logger.error(f"int 型への変換に失敗しました: {e}")

    def parse(self) -> list:
        """
        商品情報をパースする。

        Returns:
            list: パースした商品情報のリスト。
        """
        try:
            self.df.set_index("品番", inplace=True)
            self._rename_columns()
            self._remove_commas_from_numbers()
            self._convert_to_int()
        except Exception as e:
            self.logger.error(f"商品情報のパースに失敗しました: {e}")

        return self.df.to_dict("records")
