from umap import UMAP
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from hdbscan import HDBSCAN
from collections import defaultdict
from keybert import KeyBERT
from transformers import pipeline
#local models
from Scraper import scrape_reviews


embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
kw_model = KeyBERT()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# parameter for no of topic selection

def select_topic_params(n_reviews):
    if n_reviews <= 30:
        return {
            "min_cluster_size": 3,
            "min_samples": 2,
            "n_neighbors": 5
        }

    elif n_reviews <= 100:
        return {
            "min_cluster_size": 5,
            "min_samples": 3,
            "n_neighbors": 8
        }

    elif n_reviews <= 300:
        return {
            "min_cluster_size": 10,
            "min_samples": 5,
            "n_neighbors": 10
        }

    elif n_reviews <= 1000:
        return {
            "min_cluster_size": 20,
            "min_samples": 8,
            "n_neighbors": 15
        }

    else:
        return {
            "min_cluster_size": 40,
            "min_samples": 15,
            "n_neighbors": 20
        }



def bert_topic(url):
    reviews=[]
    data=scrape_reviews(url)

    for item in data:
        reviews.append(item['review'])


    params = select_topic_params(len(reviews))

    umap_model = UMAP(n_neighbors=params["n_neighbors"], n_components=5, min_dist=0.0, metric='cosine')
    hdbscan_model = HDBSCAN(
        min_cluster_size=params["min_cluster_size"],
        min_samples=params["min_samples"],
        metric="euclidean",
        cluster_selection_method="eom",
        prediction_data=True
    )

    topic_model = BERTopic(
        embedding_model=embedding_model,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        language="multilingual",
        calculate_probabilities=True,
        verbose=True
    )



    topics, probs = topic_model.fit_transform(reviews)

    topic_to_reviews = defaultdict(list)

    for review, topic in zip(reviews, topics):
        if topic != -1:   # ignore noise
            topic_to_reviews[topic].append(review)

    topic_info = topic_model.get_topic_info()

    final_topics = []

    for topic_id, revs in topic_to_reviews.items():
        final_topics.append({
            "topic_id": topic_id,
            "topic_name": topic_info[topic_info.Topic == topic_id].Name.values[0],
            "count": len(revs),
            "reviews": revs
        })

    for t in final_topics:
        #in reviews text just join 6 reviews
        reviews_text = " ".join(t["reviews"][:6])
    
        # Topic from keybert
        keywords = kw_model.extract_keywords(reviews_text, top_n=3, keyphrase_ngram_range=(1, 2))
        topic_name = ", ".join([k[0] for k in keywords])
        
        # summarize reviews
        summary = summarizer(reviews_text, max_length=50, min_length=20, do_sample=False)[0]['summary_text']
        
        # return all info like topics , name , keywords , summary
        for key, value in t.items():
            print(f"{key}: {value}")

            




if __name__ == "__main__":
    url="https://www.daraz.com.np/products/aluminium-alloy-metal-adjustable-laptop-stand-for-10-to-17-inches-mackbooklaptopstab-i105711486-s2280473603.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Astand%253Bnid%253A105711486%253Bsrc%253ALazadaMainSrp%253Brn%253Ac4deabf3a8687c12564718997054cd87%253Bregion%253Anp%253Bsku%253A105711486_NP%253Bprice%253A540%253Bclient%253Adesktop%253Bsupplier_id%253A900152409121%253Bbiz_source%253Ah5_external%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A99%253Bitem_id%253A105711486%253Bsku_id%253A2280473603%253Bshop_id%253A47403%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=5.4E%202&priceCompare=skuId%3A2280473603%3Bsource%3Alazada-search-voucher%3Bsn%3Ac4deabf3a8687c12564718997054cd87%3BoriginPrice%3A54000%3BdisplayPrice%3A54000%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767186062829&ratingscore=4.456942003514938&request_id=c4deabf3a8687c12564718997054cd87&review=1138&sale=5013&search=1&source=search&spm=a2a0e.searchlist.list.0&stock=1"
    bert_topic(url)
    






