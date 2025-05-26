from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

app = Flask(__name__)

def fetch_news(query=None, category=None):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'us',
        'q': query,
        'category': category
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('articles', [])

@app.route('/')
def home():
    query = request.args.get('q')
    category = request.args.get('category')
    articles = fetch_news(query=query, category=category)
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
