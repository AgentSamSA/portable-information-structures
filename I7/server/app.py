from flask import Flask, jsonify
from I7.server.indexer import build_index

app = Flask(__name__)

card_index = build_index()


@app.route('/cards/<name>')
def get_card(name):

    card = card_index.get(name.lower())

    if not card:
        return jsonify({'error': 'card not found'}), 404

    return jsonify(card)


@app.route('/cards')
def get_all_cards():

    return jsonify(
        sorted(card_index.values(), key=lambda c: c['cardInfo']['name'])
    )
