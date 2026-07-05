import re
import pandas as pd


class TextPreprocessor:

    @staticmethod
    def clean_dataframe(df: pd.DataFrame):

        df = df.copy()

        # Remove missing tweets
        df = df.dropna(subset=["tweet"])

        # Remove duplicates
        df = df.drop_duplicates(subset=["tweet"])

        # Normalize whitespace
        df["tweet"] = (
            df["tweet"]
            .astype(str)
            .apply(TextPreprocessor.normalize_whitespace)
        )

        return df

    @staticmethod
    def normalize_whitespace(text):

        return re.sub(r"\s+", " ", text).strip()