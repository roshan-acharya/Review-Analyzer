from collections import defaultdict
from umap import UMAP
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from keybert import KeyBERT
from transformers import pipeline
from Scraper import scrape_reviews
from Preprocessing import preprocess_reviews_to_list_roman
from Topic.sentiment import topic_sentiment

embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
kw_model = KeyBERT()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def select_topic_params(n_reviews):
    if n_reviews <= 30:
        return {"min_cluster_size": 3, "min_samples": 2, "n_neighbors": 5}
    elif n_reviews <= 100:
        return {"min_cluster_size": 5, "min_samples": 3, "n_neighbors": 8}
    elif n_reviews <= 300:
        return {"min_cluster_size": 10, "min_samples": 5, "n_neighbors": 10}
    elif n_reviews <= 1000:
        return {"min_cluster_size": 20, "min_samples": 8, "n_neighbors": 15}
    else:
        return {"min_cluster_size": 40, "min_samples": 15, "n_neighbors": 20}

def bert_topic(url):
    # Step 1: Scrape reviews
    data = scrape_reviews(url)


    if not data:
        return []

    reviews = [item['review'] for item in data]
    # Step 2: Select clustering params dynamically
    params = select_topic_params(len(reviews))

    # Step 3: Initialize UMAP and HDBSCAN
    umap_model = UMAP(n_neighbors=params["n_neighbors"], n_components=5, min_dist=0.0, metric='cosine')
    hdbscan_model = HDBSCAN(
        min_cluster_size=params["min_cluster_size"],
        min_samples=params["min_samples"],
        metric="euclidean",
        cluster_selection_method="eom",
        prediction_data=True
    )

    # Step 4: Initialize BERTopic
    topic_model = BERTopic(
        embedding_model=embedding_model,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        language="multilingual",
        calculate_probabilities=True,
        verbose=False
    )

    topics, probs = topic_model.fit_transform(reviews)

    # Step 5: Group reviews by topic
    topic_to_reviews = defaultdict(list)
    for review, topic in zip(reviews, topics):
        if topic != -1:  # ignore noise
            topic_to_reviews[topic].append(review)

    topic_info = topic_model.get_topic_info()

    # Step 6: Build final structured output
    final_topics = []
    for topic_id, revs in topic_to_reviews.items():
        # Join first 16 reviews for summarization and keywords
        reviews_text = " ".join(revs[:16])

        # KeyBERT keywords
        keywords = kw_model.extract_keywords(
            reviews_text,
            top_n=2,
            keyphrase_ngram_range=(1, 2)
        )
        keyword_list = [k[0] for k in keywords]
        topic_name = ", ".join(keyword_list)

        # Summarize reviews
        summary = summarizer(reviews_text, max_length=50, min_length=5, do_sample=False)[0]['summary_text']
        # Get sentiment for the topic
        text=preprocess_reviews_to_list_roman(reviews_text)
        topic_sent = topic_sentiment(text)

        # Append final topic dict
        final_topics.append({
            "topic_id": topic_id,
            "topic_name": topic_name,
            "keywords": keyword_list,
            "summary": summary,
            "reviews": revs,
            "count": len(revs),
            "sentiment": topic_sent
        })

    # Step 7: Return structured topics
    return final_topics
