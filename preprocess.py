import pandas as pd
import joblib
import warnings
import warnings

import joblib
import pandas as pd

warnings.filterwarnings('ignore')

print("........Initialization Started........")

# Reading the pre-processed file after text cleaning and processing.
data = pd.read_csv("data/sample30_p.csv", encoding='ISO-8859-1', low_memory=False)
useful_list = ['id', 'name', 'reviews_rating', 'user_sentiment', 'review_title_text']
data = data[useful_list]

print("Load supported pickles. Sentimental, Recommendating & Vectorizer pickles.")

senti_model = joblib.load("models/rf_model.pkl")
recomd_model = joblib.load("models/user_user.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

print("........Initialization Complete........")
print()


def get_data():
    return data


def get_sentiment_model():
    return senti_model


def get_recommend_model():
    return recomd_model


def get_vectorizer():
    return vectorizer
