import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()


class LLMClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(api_key=api_key)

        # You can change this in one place if needed
        self.model = "gemini-2.5-flash"

        self.max_retries = 5

    def generate(self, prompt: str) -> str:

        for attempt in range(self.max_retries):

            try:

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )

                return response.text.strip()

            except errors.ServerError:

                wait = 2 ** attempt

                print(
                    f"Gemini server busy. "
                    f"Retrying in {wait} seconds..."
                )

                time.sleep(wait)

            except errors.ClientError as e:

                print(f"Gemini Client Error: {e}")

                raise

            except Exception as e:

                print(f"Unexpected Error: {e}")

                raise

        raise RuntimeError(
            "Gemini API failed after multiple retries."
        )