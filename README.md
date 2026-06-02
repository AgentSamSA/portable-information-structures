# Scryfall API Portability Assistant
This repository is intended to serve as a collection for various files, code, and documentation related the Scryfall API Portability Assistant.

## Information Story
[Scryfall](https://scryfall.com/) is a powerful, online _Magic: The Gathering_ card search engine. It features a query system that lets anyone search up any card that currently exists in the _Magic_ trading card game. It also features a [REST-like API](https://scryfall.com/docs/api) that allows for more programmatic handling of the data.

While incredibly useful for anyone interested or involved with _Magic_, there are some limitations with getting data from the card search feature and the API. Namely:
- unable to export search data from the traditional UI
- API requires technical knowledge in both how to request the data as well as concepts specific to Scryfall (e.g. the query language)
- limited options when exporting the data

These considerations are what inspired me to create a portability assistant for Scryfall.

## Current Progress
The project is currently in a greatly unfinished state. Namely, the main function components right now are the dataset downloader and the flask server.

The dataset downloader is located inside a jupyter notebook inside `I3`. It is also used to download the `default-cards` bulk dataset that the flask server uses.  
The notebook includes some other code, include a method that attempts to map Scryfall-like queries onto regular `pandas` Dataframe operations, allowing users familiar with Scryfall query syntax to filter the dataset that way. The resulting data can then be downloaded by uncommenting the last two lines in the final code cell and then running that cell once variables have been established.

The flask server's most up-to-date version is located in `I8`. It supports several endpoints, explored in more detail in that section. To run the server:
```
git clone https://github.com/AgentSamSA/portable-information-structures.git
cd portable-information-structures/I8
pip install -r requirements.txt
```
Running this server in a virtual environment is recommended, which you can do via
```
python -m venv .venv
source .venv/bin/activate
```
