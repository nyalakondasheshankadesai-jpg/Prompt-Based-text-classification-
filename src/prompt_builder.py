from pathlib import Path


class PromptBuilder:
    """
    Builds prompts for different prompting strategies.

    Supports:
    - Single tweet prompting
    - Batch prompting
    """

    def __init__(self, prompt_folder="prompts"):
        self.prompt_folder = Path(prompt_folder)

    def load_prompt(self, strategy: str) -> str:
        """
        Load the prompt template.
        """
        file = self.prompt_folder / f"{strategy}.txt"

        if not file.exists():
            raise FileNotFoundError(f"Prompt not found: {file}")

        return file.read_text(encoding="utf-8")

    def build(self, strategy: str, tweet: str) -> str:
        """
        Build prompt for a single tweet.
        """
        template = self.load_prompt(strategy)

        return template.replace("{{tweet}}", tweet)

    def build_batch(self, strategy: str, tweets: list[str]) -> str:
        """
        Build prompt for multiple tweets.
        """

        template = self.load_prompt(strategy)

        formatted = []

        for idx, tweet in enumerate(tweets, start=1):
            formatted.append(f"{idx}. {tweet}")

        tweet_block = "\n".join(formatted)

        return template.replace("{{tweets}}", tweet_block)