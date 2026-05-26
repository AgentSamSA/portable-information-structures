import random
from flask import Flask, jsonify, request
from server.indexer import build_index

app = Flask(__name__)

card_index = build_index()


# Returns a card with the specified name
@app.route('/cards/<name>')
def get_card(name):

    card = card_index.get(name.lower())

    if not card:
        return jsonify({'error': 'card not found'}), 404

    return jsonify(card)


# Returns all cards
@app.route('/cards')
def get_all_cards():

    return jsonify(
        sorted(card_index.values(), key=lambda c: c['cardInfo']['name'])
    )


# Gets a random card
@app.route('/cards/random')
def random_card():
    return jsonify(random.choice(list(card_index.values())))


# Search for a card by name or oracle text (?={your query})
@app.route('/cards/search')
def search_cards():
    q = request.args.get('q', '').lower()

    results = [
        card for card in card_index.values()
        if q in card['cardInfo']['name'].lower()
        or q in (card['cardInfo']['oracleText'] or '').lower()
    ]

    return jsonify(results[:30])


# Filter cards by color (?color={color})
@app.route('/cards/filter')
def filter_cards():
    color = request.args.get('color', '').upper()

    results = [
        card for card in card_index.values()
        if color in card['gameplayInfo']['colors']
    ]

    return jsonify(results[:30])

# Recommend cards based on color and max mana value (?color={color}&max_cmc={cmc})
@app.route('/cards/recommend')
def recommend():
    color = request.args.get('color', '').upper()
    max_cmc = float(request.args.get('max_cmc', 999))

    results = [
        card for card in card_index.values()
        if color in card['gameplayInfo']['colors']
        and card['cardInfo']['cmc'] is not None
        and card['cardInfo']['cmc'] <= max_cmc
    ]

    return jsonify(results[:20])