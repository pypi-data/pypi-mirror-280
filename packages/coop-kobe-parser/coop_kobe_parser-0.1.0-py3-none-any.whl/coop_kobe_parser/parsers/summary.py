from pandas import Series


class SummaryParser:
    """
    支払情報をパースするクラス。

    Attributes:
        df (Series): 支払情報のデータフレーム。
    """

    def __init__(self, df: Series):
        """
        SummaryParser クラスの初期化。

        Args:
            df (pd.Series): 商品情報のデータフレーム。
        """
        # 必要な列（"商品名", "数量", "小計"）だけを抽出
        self.df = df.reset_index(drop=True)[["商品名", "数量", "小計"]]

    def _get_value(self, item, column="小計"):
        """
        値を数値に変換する
        """
        try:
            value = self.df.loc[self.df["商品名"] == item, column].values[0]
            return int(value.replace(",", ""))
        except IndexError:
            raise ValueError(f"'{item}' がデータフレームに存在しません。")
        except ValueError:
            raise ValueError(f"'{item}' の '{column}' 列の値が数値に変換できません。")

    def parse(self) -> dict[str, int]:
        """
        支払情報を抽出し、辞書として返却する。
        """
        items = {
            "pre_total_8": "値引き前本体合計金額(8%)",
            "discount_8": "値引き額(8%)",
            "total_8": "本体合計金額(8%)",
            "tax_8": "消費税(8%)",
            "pre_total_10": "値引き前本体合計金額(10%)",
            "discount_10": "値引き額(10%)",
            "total_10": "本体合計金額(10%)",
            "tax_10": "消費税(10%)",
            "pre_total_non_tax": "値引き前本体合計金額（非課税）",
            "discount_non_tax": "値引き額(非課税)",
            "total_non_tax": "本体合計金額(非課税)",
            "total_amount": "本体合計金額",
            "total_tax": "消費税等",
            "order_amount_incl_tax": "ご注文金額(税込)",
            "expected_points": "獲得予定ポイント",
            "total_items": ("合計点数", "数量"),
        }

        return {
            k: self._get_value(*v) if isinstance(v, tuple) else self._get_value(v)
            for k, v in items.items()
        }
