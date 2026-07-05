import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import pandas as pd


class Visualizer:

    @staticmethod
    def plot_confusion_matrix(cm, labels, output_file):

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=labels,
        )

        disp.plot()

        plt.tight_layout()

        plt.savefig(output_file)

        plt.close()

    @staticmethod
    def plot_strategy_comparison(results, output_file):

        df = pd.DataFrame(results)

        plt.figure(figsize=(8,5))

        plt.bar(df["Strategy"], df["Accuracy"])

        plt.title("Prompt Strategy Comparison")

        plt.ylabel("Accuracy")

        plt.xlabel("Prompt Strategy")

        plt.tight_layout()

        plt.savefig(output_file)

        plt.close()