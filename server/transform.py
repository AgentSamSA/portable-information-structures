# Transform each card into improved JSON structure
def transform_card(card):

    legalities = card.get('legalities', {})
    
    legal_formats = [
        fmt for fmt, status in legalities.items()
        if status == 'legal'
    ]

    return {
        'cardInfo': {
            'cardId': card.get('id'),
            'name': card.get('name'),
            'manaCost': card.get('mana_cost'),
            'cmc': card.get('cmc'),
            'typeLine': card.get('type_line'),
            'oracleText': card.get('oracle_text'),
        },
        'marketInfo': {
            'usdPrice': float(card['prices']['usd'])
            if card.get('prices', {}).get('usd')
            else None,
            'eurPrice': float(card['prices']['eur'])
            if card.get('prices', {}).get('eur')
            else None,
        },
        'gameplayInfo': {
            'colors': card.get('colors', []),
            'keywords': card.get('keywords', []),
            'legalities': legal_formats,
        },
        'metadata': {'schemaVersion': '1.0', 'source': 'Scryfall API'},
        'accessControl': {'accessLevel': 'read-only'},
    }
