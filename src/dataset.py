import pandas as pd


class DatasetLoader:
    """
    Loads Twitter sentiment datasets.
    """

    def __init__(self, train_path: str, validation_path: str):
        self.train_path = train_path
        self.validation_path = validation_path

    def load_train(self):
        df = pd.read_csv(self.train_path)
        return self._prepare(df)

    def load_validation(self):
        df = pd.read_csv(self.validation_path)
        return self._prepare(df)

    def _prepare(self, df):

        # Twitter dataset format:
        # 0 = Tweet ID
        # 1 = Entity
        # 2 = Sentiment
        # 3 = Tweet

        df.columns = [
            "tweet_id",
            "entity",
            "sentiment",
            "tweet"
        ]

        return df