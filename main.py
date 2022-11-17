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
    if request.method == 'POST':
        people = ''
        number= ''
        response = requests.get(f"https://swapi.py4e.com/api/{people}/{number}/")
        data = response.json()

        context = {
            
        }


@app.route('/films')
def film_page():
    """
    Displays the film page for SWAPI
    """
    return render_template('films.html')

@app.route('/planets')
def planet_page():
    """
    Displays the planet page for SWAPI
    """
    return render_template('planets.html')

@app.route('/vehicles')
def vehicle_page():
    """
    Displays the vehicle page for SWAPI
    """
    return render_template('vehicles.html')


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=3000)
