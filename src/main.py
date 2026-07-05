import yaml
import pandas as pd
from tqdm import tqdm

from dataset import DatasetLoader
from preprocessing import TextPreprocessor
from prompt_builder import PromptBuilder
from llm_client import LLMClient
from parser import PredictionParser
from evaluator import Evaluator
from visualization import Visualizer
from report_generator import ReportGenerator

# ------------------------------
# Load Config
# ------------------------------

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

loader = DatasetLoader(
    config["dataset"]["train"],
    config["dataset"]["validation"]
)

df = loader.load_validation()

df = TextPreprocessor.clean_dataframe(df)

df = df.head(config["sample_size"])

builder = PromptBuilder()

client = LLMClient()

strategies = config["experiment"]["strategies"]

comparison_results = []

# Number of tweets per API request
BATCH_SIZE = 10


for strategy in strategies:

    print("\n" + "=" * 60)
    print(f"Running Strategy : {strategy}")
    print("=" * 60)

    predictions = []
    truths = []

    # Process dataset in batches
    for start in tqdm(range(0, len(df), BATCH_SIZE)):

        batch = df.iloc[start:start + BATCH_SIZE]

        tweets = batch["tweet"].tolist()

        truths.extend(batch["sentiment"].tolist())

        prompt = builder.build_batch(
            strategy,
            tweets
        )

        response = client.generate(prompt)

        batch_predictions = PredictionParser.parse_batch(response)

        # Safety check
        if len(batch_predictions) != len(batch):

            print(
                f"Warning: Expected {len(batch)} predictions "
                f"but got {len(batch_predictions)}"
            )

            # Fill missing predictions
            while len(batch_predictions) < len(batch):
                batch_predictions.append("Unknown")

            batch_predictions = batch_predictions[:len(batch)]

        predictions.extend(batch_predictions)

    # -----------------------------
    # Evaluation
    # -----------------------------

    metrics, cm = Evaluator.evaluate(
        truths,
        predictions
    )

    metrics["Strategy"] = strategy

    comparison_results.append(metrics)

    # -----------------------------
    # Save Predictions
    # -----------------------------

    output_df = df.copy()

    output_df["Prediction"] = predictions

    output_df.to_csv(
        f"outputs/{strategy}_predictions.csv",
        index=False
    )

    Evaluator.save_metrics(
        metrics,
        f"outputs/{strategy}_metrics.csv"
    )

    Visualizer.plot_confusion_matrix(
        cm,
        ["Positive", "Negative", "Neutral"],
        f"outputs/{strategy}_cm.png"
    )

# -----------------------------
# Compare Strategies
# -----------------------------

Visualizer.plot_strategy_comparison(
    comparison_results,
    "outputs/strategy_comparison.png"
)
ReportGenerator.generate(
    comparison_results,
    output_folder="outputs"
)

print("\nExperiment Completed Successfully!")