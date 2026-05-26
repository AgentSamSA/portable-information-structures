# mtg-cards-flask-server
A small API that returns Magic: The Gathering card information from Scryfall, built with Flask.

## Setup
```
git clone https://github.com/AgentSamSA/mtg-cards-flask-server.git
cd your-repo
pip install -r requirements.txt
```
You may choose to run this project in a virtual environment so that you can install the requirements only for this project.

To run the flask server locally, use `flask run`. You can use `-p` to specific a port (such as `port 5002`).  
You can use `python server/test_client.py` inside the root directory to test some API calls.

## Endpoints
`/card/{card}`  
Returns a json object for a *Magic: The Gathering* card with the specified name from Scryfall's API.

`/cards`  
Returns a list of json objects for every *Magic: The Gathering* card. WARNING: maybe be slow due to the size of the dataset (>500MB).

`/cards/random`
Returns a random card.

`/cards/search`
Returns cards based on if the search term is in the name or in the card's oracle text.

`/cards/filter`
Filters cards by their color.

`/cards/recommend`
Recommends a card for you based on the color and max mana value.
