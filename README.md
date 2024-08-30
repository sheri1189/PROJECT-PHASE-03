# Toxicity Detection System

## Overview
This project is a toxicity detection system that uses BERT for classifying the toxicity of comments and replaces toxic words with non-toxic synonyms. It tracks user profiles, including toxic word usage and comment history.

## Setup
1. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Structure
- `app.py`: Main Streamlit application.
- `model/`: Contains model and tokenizer loading functions.
- `utils/`: Contains utility functions for toxicity classification and profile management.
- `data/`: Stores user profiles and data.
- `requirements.txt`: Lists project dependencies.
- `README.md`: Project overview and instructions.
