# Scryfall API Portability Assistant Flask Server

This flask server hosts an API with several endpoints serving the Scryfall API Portability Assistant project.

## Setup
```
git clone https://github.com/AgentSamSA/portable-information-structures.git
cd I7
pip install -r requirements.txt
```
To run the flask server locally, use `flask run`. You can use `-p` to specific a port (such as `port 5002`).

You can use `python server/test_client.py` inside the working directory to test some API calls.

## Endpoints
`/card/{card}`  
Returns an json object for a *Magic: The Gathering* card with the specified name from Scryfall's own API.

`/cards`  
Returns a list of json objects for every *Magic: The Gathering* card. WARNING: maybe be slow due to the size of the dataset (>500MB).
