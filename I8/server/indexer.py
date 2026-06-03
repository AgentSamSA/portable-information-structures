from .loader import stream_cards
from .transform import transform_card

# Build index of cards for faster lookup
def build_index():
    
    index = {}
    
    for card in stream_cards():
        
        name = card.get('name', '').lower()
        
        index[name] = transform_card(card)
        
    return index

if __name__ == '__main__':
    build_index()