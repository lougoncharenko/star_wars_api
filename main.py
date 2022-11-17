import requests
from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def home_page():
    """
    Displays the homepage with forms for weather data.
    """
    pass


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=3000)