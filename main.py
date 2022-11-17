import requests
from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def home_page():
    """
    Displays the homepage for starwars app
    """
    return render_template('home.html')


@app.route('/char')
def character_page():
    """
    Displays the the character page for SWAPI
    """
    return render_template('char.html')


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=3000)
