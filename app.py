from flask import Flask, jsonify, request, render_template

from model import get_top05_recommendations

app = Flask(__name__)


# Default view
@app.route('/')
def home():
    return render_template('index.html')


# API to test
@app.route("/recommend_api/<user_name>", methods=['GET'])
def recommend_api(user_name):
    data = get_top05_recommendations(user_name)
    return jsonify(data.values.tolist())


# Recommend call, if its get, default view is given.
@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    try:
        if request.method == 'POST':
            user_name = request.form['user_name']
            if user_name and not user_name.isspace():
                data = get_top05_recommendations(user_name.lower())
                data.rename(columns={'name': 'Product Name', 'pos_percent': 'Recommendation Score (%) '}, inplace=True)
                text = "Top Product Recommendations for     <i>" + user_name + "</i>"
                return render_template('index.html', table=data.to_html(index=False), text2=text)
        return render_template('index.html')
    except:
        text = "Could not find the user  <i>" + user_name + "</i>  in the system , try with a valid user name"
        return render_template('index.html', text2=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
