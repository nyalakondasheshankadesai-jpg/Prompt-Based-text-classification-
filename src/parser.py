import json
import re


class PredictionParser:

    VALID = {
        "positive": "Positive",
        "negative": "Negative",
        "neutral": "Neutral"
    }

    @staticmethod
    def parse_batch(response):

        try:

            # Remove markdown fences
            response = response.replace("```json", "")
            response = response.replace("```", "")

            # Extract JSON array
            match = re.search(
                r"\[[\s\S]*\]",
                response
            )

            if not match:
                raise ValueError("No JSON array found.")

            data = json.loads(match.group())

            predictions = []

            for item in data:

                label = item["label"].lower()

                predictions.append(
                    PredictionParser.VALID.get(
                        label,
                        "Unknown"
                    )
                )

            return predictions

        except Exception as e:

            print("Parser Error:", e)

            return []