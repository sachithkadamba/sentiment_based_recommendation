import pandas as pd

from preprocess import get_data
from preprocess import get_recommend_model
from preprocess import get_sentiment_model
from preprocess import get_vectorizer

data = get_data()
sentiment_model = get_sentiment_model()
recomdation_model = get_recommend_model()
vectorizer = get_vectorizer()


def get_top_20_products(username):
    return recomdation_model.loc[username].sort_values(ascending=False)[0:20]


def get_top_5_recommendations(username):
    recom_list = get_top_20_products(username)
    print(recom_list)
    cl = {'name': [], 'pos_percent': []}
    op = pd.DataFrame(cl)
    for product_id in recom_list.index:
        value = get_sentiment_ratings(product_id)
        op = op.append(value, ignore_index=True)
    return op.sort_values(by=['pos_percent', 'name'], ascending=[False, True]).iloc[:5, :]


def get_sentiment_ratings(product_id):
    dat = data[data.id == product_id]
    pos_per = calculate_top(dat)
    return {'name': dat['name'].unique()[0], 'pos_percent': pos_per}


def calculate_top(dat):
    output = sentiment_model.predict(vectorizer.transform(dat['review_title_text']))
    pos = 0
    neg = 0
    for out in output:
        if out == 1:
            pos = pos + 1
        else:
            neg = neg + 1
    return round((pos / (pos + neg)) * 100, 2)
