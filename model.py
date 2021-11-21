import pandas as pd

from preprocess import get_data
from preprocess import get_recommend_model
from preprocess import get_sentiment_model
from preprocess import get_vectorizer

# Getting the initialized pickle and data from preprocessing.
data = get_data()
senti_model = get_sentiment_model()
recomd_model = get_recommend_model()
vectorizer = get_vectorizer()


# Get top 20 products for the provided user name.
def get_top20_products(username):
    return recomd_model.loc[username].sort_values(ascending=False)[0:20]


# Get Top 5 products, this function calls the recommendation system
# for 20 results then enhances it by taking top 5 from sentiment system.
def get_top05_recommendations(username):
    recom_list = get_top20_products(username)
    print("Top 20 product Ids with score from recommendation system")
    print(recom_list)
    cl = {'name': [], 'pos_percent': []}
    op = pd.DataFrame(cl)
    for product_id in recom_list.index:
        value = get_sentiment_ratings(product_id)
        op = op.append(value, ignore_index=True)
    return op.sort_values(by=['pos_percent', 'name'], ascending=[False, True]).iloc[:5, :]


# Function to get the product details and positive sentiment score.
def get_sentiment_ratings(product_id):
    dat = data[data.id == product_id]
    pos_per = calculate_top(dat)
    return {'name': dat['name'].unique()[0], 'pos_percent': pos_per}


# Helper function to calculate the positive sentiment percent.
def calculate_top(dat):
    output = senti_model.predict(vectorizer.transform(dat['review_title_text']))
    pos = 0
    neg = 0
    for out in output:
        if out == 1:
            pos = pos + 1
        else:
            neg = neg + 1
    return round((pos / (pos + neg)) * 100, 2)

# Testing
# print(get_top05_recommendations('josh'))
