import pandas as pd
import string
import emoji
import re
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import nltk
from nltk.stem import WordNetLemmatizer
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


nltk.download('words')
nltk.download('stopwords')
nltk.download('wordnet')


from nltk.corpus import words, stopwords

ENGLISH_WORDS = set(words.words())
EN_STOPWORDS = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()



ROMAN_TO_DEVANAGARI = {
    "xa": "छ",
    "xaina": "छैन",
    "cha": "छ",
    "chha": "छ",
    "ramro": "राम्रो",
    "ramroo": "राम्रो",
    "dhilo": "ढिलो",
    "dherai": "धेरै",
}


# Detect if a word is all Latin letters

def is_latin(word):
    return all(ord(c) < 128 for c in word)


def is_english(word):
    lemma = lemmatizer.lemmatize(word)
    return lemma in ENGLISH_WORDS


def emoji_to_text(text):
    return emoji.demojize(text)

def handling_symbol(text):
    text = text.replace(":", "")
    return text.replace("_"," ")



def remove_punctuation(text):
  translator = str.maketrans('', '', string.punctuation)
  return text.translate(translator)


def normalize_word(word):


    word_lower = re.sub(r'(.)\1{2,}', r'\1\1', word)
    
    if word_lower in EN_STOPWORDS:
        return ""

    if is_latin(word) and not is_english(word):
        if word_lower in ROMAN_TO_DEVANAGARI:

            return ROMAN_TO_DEVANAGARI[word_lower]
     
        try:
            return transliterate(word, sanscript.ITRANS, sanscript.DEVANAGARI)
        except:
            return word
    else:
      
        return word

#NORMALIZE FULL REVIEW
def normalize_review(text):
    words_list = text.split()
    normalized_words = [normalize_word(w) for w in words_list if normalize_word(w) != ""]
    return ' '.join(normalized_words)



def preprocess(path):
    combined_df=pd.read_csv(path)
    combined_df['review']=combined_df['review'].astype(str) #convert review to string
    combined_df['review']=combined_df['review'].apply(lambda x:x.lower()) #lowercase conversion
    combined_df['review']=combined_df['review'].apply(remove_punctuation) #remove punctuations
    combined_df['review']=combined_df['review'].apply(emoji_to_text) # convert emoji to its corresponding meaning
    combined_df['review']=combined_df['review'].apply(handling_symbol) #handle symbol like :,_ from emoji
    return combined_df

def clean_data(path):
    save_path=BASE_DIR / 'Data/Cleaned/review.csv'
    combined_df=preprocess(path)
    combined_df.to_csv(save_path,index=False)


    



def preprocess_reviews_to_list_roman(reviews):

    normalized_reviews = []

    for review in reviews:
        if not isinstance(review, str) or review.strip() == "":
            continue

        text = review.lower()
        text = emoji.demojize(text)            # emoji -> :smile:
        text = text.replace("_", " ").replace(":", "")  # clean emoji text
        text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation


    return text


    