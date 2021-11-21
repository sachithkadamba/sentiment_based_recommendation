from flask import Flask, jsonify, request, render_template

from model import get_top_5_recommendations

app = Flask(__name__)


# Default view
@app.route('/')
def home():
    return render_template('index.html')


# Recommend call, if its get, default view is given.
@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    try:
        if request.method == 'POST':
            user_name = request.form['user_name']
            if user_name and not user_name.isspace():
                data = get_top_5_recommendations(user_name.lower())
                data.rename(columns={'name': 'Product Name', 'pos_percent': 'Recommendation Score (%) '}, inplace=True)
                text = "Product Recommendations for     <i>" + user_name + "</i>"
                return render_template('index.html', table=data.to_html(index=False), text2=text)
        return render_template('index.html')
    except:
        text = "We dont the user  <i>" + user_name + "</i>  in the system , please enter valid user name"
        return render_template('index.html', text2=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
