from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
)
import pandas as pd


class Evaluator:

    LABELS = [
        "Positive",
        "Negative",
        "Neutral",
    ]

    @staticmethod
    def evaluate(y_true, y_pred):

        accuracy = accuracy_score(y_true, y_pred)

        precision, recall, f1, _ = precision_recall_fscore_support(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        )

        cm = confusion_matrix(
            y_true,
            y_pred,
            labels=Evaluator.LABELS
        )

        metrics = {
            "Accuracy": accuracy,
            "Precision": precision,
            "Recall": recall,
            "F1 Score": f1,
        }

        return metrics, cm

    @staticmethod
    def save_metrics(metrics, filename):

        df = pd.DataFrame([metrics])

        df.to_csv(filename, index=False)