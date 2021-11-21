import pandas as pd
import joblib
import warnings
import warnings

import joblib
import pandas as pd

warnings.filterwarnings('ignore')


data = pd.read_csv("data/sample30_processed.csv", encoding='ISO-8859-1', low_memory=False)
column_list = ['id', 'name', 'reviews_rating', 'user_sentiment', 'review_title_text']
data = data[column_list]


sentiment_model = joblib.load("models/rf_model.pkl")
recomdation_model = joblib.load("models/user_user.pkl")
the_vectorizer = joblib.load("models/vectorizer.pkl")


def get_data():
    return data


def get_sentiment_model():
    return sentiment_model


def get_recommend_model():
    return recomdation_model


def get_vectorizer():
    return the_vectorizer
