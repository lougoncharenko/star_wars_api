import requests
import os
from dotenv import load_dotenv
import json
from flask import Flask, render_template, request, send_file
import random
app = Flask(__name__)

load_dotenv()
apikey = os.getenv('API_KEY')

@app.route('/')
def home_page():
    """
    Displays the homepage for starwars app
    """
    return render_template('home.html')

@app.route('/char', methods=['GET', 'POST'])
def character_page():
    """
    Displays the the character page for SWAPI
    """
    character_id = request.args.get('character-id')
    limit = 1
    if not character_id:
        character_id = '1'
    response = requests.get(f"https://swapi.py4e.com/api/people/{character_id}/")
    character_data = response.json()
    try:
        films = [requests.get(film).json()['title'] for film in character_data['films']]
    except KeyError:
        print('KeyError: Films Not Found')
        films = ['N/A']
    try:
        character_name = character_data['name']
    except KeyError:
        print('KeyError: Character Not Found')
        character_name = 'star wars'
    response = requests.get(
        f"https://tenor.googleapis.com/v2/search?q={character_name}&key={apikey}&limit={limit}")
    gifs = json.loads(response.content).get('results')
    context = {
    "character": character_data,
    'films': films,
    'gifs': gifs
    }
    return render_template('char.html', **context)
    


@app.route('/films')
def film_page():
    """
    Displays the film page for SWAPI
    """
    number = random.randint(1, 7)
    response = requests.get(f"https://swapi.py4e.com/api/films/{number}/")
    data = response.json()
    context = {
    "film": data
    }
    return render_template('films.html', **context)

@app.route('/planets')
def planet_page():
    """
    Displays the planet page for SWAPI
    """
    number = random.randint(1, 62)
    response = requests.get(f"https://swapi.py4e.com/api/planets/{number}/")
    data = response.json()
    context = {
    "planet": data,
    }
    return render_template('planets.html', **context)

@app.route('/vehicles')
def vehicle_page():
    """
    Displays the vehicle page for SWAPI
    """
    number = random.randint(1, 7)
    response = requests.get(f"https://swapi.py4e.com/api/vehicles/{number}/")
    data = response.json()
    context = {
    "vehicle": data,
    }
    return render_template('vehicles.html', **context)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=3000)
