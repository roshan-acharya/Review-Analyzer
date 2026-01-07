from Preprocessing import preprocess, clean_data
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

if __name__=="__main__":
    read_path=BASE_DIR / 'Data/sentiment.csv'
    clean_data(read_path)
