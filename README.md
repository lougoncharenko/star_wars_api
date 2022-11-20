<div align="center">

# Star Wars App

</div>

## About the Project:
- This is a star wars web application that allows users to search for a character to get character information and a gif related to the character.

### Core Technologies

- `Python`
- `Flask`
- `Json`
- `HTML`
- `CSS`

## Features
- Incorporates [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/) to build a server that takes form requests
- Incorporates [Star Wars API](https://swapi.dev) to fetch a  character information based on user selection.
- Incorporates [Tenor API](https://tenor.com/gifapi/documentation) to grab a gif that corresponds with the character retrieved from the star wars api.


### File Structure

```sh
Star_Wars_Api/
├── static         # Directory for Styling page
├── templates # Directory for reusable HTML templates
├── main.py        # File that runs the flask server to create routes and run applications 
```