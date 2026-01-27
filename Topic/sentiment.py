from transformers import pipeline
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = 'notebook/models/xlm-finetuned-sentiment-save'
sentiment_model = pipeline(
    "text-classification",
    model=model_path,
    tokenizer=model_path,
    device=0,
)


def topic_sentiment(reviews):
    results = sentiment_model(reviews, truncation=True)
    labels = []
    for r in results:
        label = r['label'].lower()
        labels.append(label)
    # Majority vote
    overall_sentiment = "positive" if labels.count("positive") >= labels.count("negative") else "negative"

    return overall_sentiment


