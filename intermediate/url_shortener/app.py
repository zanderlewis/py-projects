# Requirements: Flask
# Difficulty: VII

from flask import Flask, request, render_template, redirect
import string
import random

app = Flask(__name__)
url_mapping = {}  # In a real-world scenario, this would be stored in a database

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        while True:
            short_url = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=5))
            if short_url not in url_mapping:
                url_mapping[short_url] = original_url
                break
        return f'Short URL is: {request.url_root}{short_url}'
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    return redirect(url_mapping.get(short_url, '/'))

if __name__ == '__main__':
    app.run(debug=True)