Prompt-Based Sentiment Classification using Large Language Models
Project Overview

This project implements a Prompt-Based Text Classification System that performs sentiment analysis on Twitter data using Large Language Models (LLMs) instead of conventional machine learning or deep learning models.

Unlike traditional text classification approaches that require model training, feature extraction, and optimization, this project relies entirely on Prompt Engineering to guide a Large Language Model in predicting the sentiment of tweets.

The project compares multiple prompting techniques to evaluate how prompt design influences classification performance.

Objectives

The primary objectives of this project are:

Build a sentiment classification system without training a machine learning model.
Utilize Large Language Models through API calls.
Compare different prompt engineering strategies.
Evaluate the effectiveness of each prompting strategy using standard classification metrics.
Generate visualizations and reports for performance comparison.
Dataset

This project uses the Twitter Sentiment Analysis Dataset obtained from Kaggle.

The dataset contains:

Tweets
Corresponding sentiment labels

Possible sentiment classes are:

Positive
Negative
Neutral
Prompt Engineering Strategies

The project evaluates five prompting strategies.

1. Zero-Shot Prompting

The model receives only task instructions without any examples.

Example:

Classify the following tweets into Positive, Negative, or Neutral.

Purpose:

Tests the model's inherent reasoning capability.
2. Few-Shot Prompting

The prompt contains several labeled examples before the actual tweets.

Example:

Tweet:
I love this phone.
Label:
Positive

Tweet:
Worst experience ever.
Label:
Negative

Purpose:

Helps the model understand the expected classification pattern.
3. Role Prompting

The model is assigned a professional role.

Example:

You are an expert social media sentiment analyst.

Purpose:

Encourages the model to adopt domain-specific reasoning.
4. Chain-of-Thought Prompting

The model is instructed to internally analyze emotion, tone, sarcasm, and context before deciding the sentiment.

Purpose:

Improves reasoning quality while hiding intermediate reasoning from the output.
5. Constrained Prompting

The model is forced to choose from a fixed set of labels.

Allowed labels:

Positive
Negative
Neutral

Purpose:

Reduces inconsistent outputs.
Technologies Used

Programming Language

Python 3.11+

Libraries

pandas
scikit-learn
matplotlib
PyYAML
python-dotenv
tqdm
google-genai

LLM

Google Gemini API
Project Structure
Prompt-Based-Text-Classifier/

│
├── config.yaml
├── requirements.txt
├── .env
│
├── data/
│   ├── twitter_training.csv
│   └── twitter_validation.csv
│
├── prompts/
│   ├── zero_shot.txt
│   ├── few_shot.txt
│   ├── role.txt
│   ├── chain_of_thought.txt
│   └── constrained.txt
│
├── outputs/
│
├── src/
│   ├── main.py
│   ├── dataset.py
│   ├── preprocessing.py
│   ├── prompt_builder.py
│   ├── llm_client.py
│   ├── parser.py
│   ├── evaluator.py
│   └── visualization.py
│
└── README.md
System Workflow
Dataset
     │
     ▼
Data Loading
     │
     ▼
Preprocessing
     │
     ▼
Prompt Builder
     │
     ▼
Gemini API
     │
     ▼
Prediction Parser
     │
     ▼
Evaluation
     │
     ▼
Graphs & CSV Reports
Preprocessing

Before sending tweets to the LLM, the dataset is cleaned by:

Removing duplicate records
Removing missing values
Normalizing whitespace
Preserving hashtags
Preserving punctuation
Preserving emojis

No aggressive text cleaning is performed because these elements contribute to sentiment.

Batch Prompting

Instead of sending one API request per tweet, this project uses Batch Prompting.

Example:

Tweet 1

Tweet 2

Tweet 3

Tweet 4

Tweet 5

The LLM returns a JSON array containing predictions for all tweets.

Advantages:

Fewer API calls
Faster execution
Lower API cost
Better scalability
Evaluation Metrics

The project evaluates predictions using:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Output Files

The project automatically generates:

outputs/

zero_shot_predictions.csv
zero_shot_metrics.csv
zero_shot_cm.png

few_shot_predictions.csv
few_shot_metrics.csv
few_shot_cm.png

role_predictions.csv
role_metrics.csv
role_cm.png

chain_of_thought_predictions.csv
chain_of_thought_metrics.csv
chain_of_thought_cm.png

constrained_predictions.csv
constrained_metrics.csv
constrained_cm.png

strategy_comparison.png
Configuration

Project parameters can be modified through config.yaml.

Example:

sample_size: 100

batch_size: 10

model:
  provider: gemini
  name: gemini-2.5-flash
Installation

Clone the repository.

git clone <repository-url>

Navigate to the project.

cd Prompt-Based-Text-Classifier

Create a virtual environment.

python -m venv .venv

Activate the environment.

Windows:

.venv\Scripts\activate

Install dependencies.

pip install -r requirements.txt
API Configuration

Create a .env file.

GEMINI_API_KEY=YOUR_API_KEY

Obtain a Gemini API key from Google AI Studio.

Running the Project

Execute:

python src/main.py

or

python -m src.main
Expected Outputs

The application performs the following steps:

Loads the dataset.
Cleans the data.
Builds prompts for each prompting strategy.
Sends batched requests to the Gemini API.
Parses JSON predictions.
Evaluates predictions.
Saves metrics and prediction files.
Generates confusion matrices.
Produces a strategy comparison chart.
Advantages of Prompt Engineering

Compared to traditional machine learning, prompt engineering offers several benefits:

No model training required
No GPU-intensive training process
Easy to modify task behavior by changing prompts
Rapid experimentation with different prompting strategies
Leverages the reasoning capabilities of state-of-the-art LLMs
Limitations
Requires internet connectivity.
Depends on the availability and quota of the Gemini API.
Performance may vary depending on the LLM version.
API latency can affect execution time.
Results depend on prompt quality.
Future Enhancements

Potential improvements include:

Support for multiple datasets (e.g., AI-generated text detection, AG News).
Multi-language sentiment classification.
Additional prompting techniques such as Self-Consistency and ReAct prompting.
Interactive web interface using Streamlit or Flask.
Automated HTML report generation.
Support for multiple LLM providers (OpenAI, Anthropic, Azure OpenAI).
Conclusion

This project demonstrates how Prompt Engineering can effectively solve text classification tasks without training a dedicated machine learning model. By comparing multiple prompting strategies—including Zero-Shot, Few-Shot, Role Prompting, Chain-of-Thought, and Constrained Prompting—it highlights the impact of prompt design on Large Language Model performance. The project also provides quantitative evaluation through standard classification metrics and visualizations, making it a practical framework for studying prompt engineering techniques in real-world natural language processing applications.