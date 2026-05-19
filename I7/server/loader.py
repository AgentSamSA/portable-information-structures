from pathlib import Path
import ijson

DATA_PATH = Path('data/default-cards.json')

# Ensure raw dataset exists, otherwise call download function
def ensure_dataset():
    if not DATA_PATH.exists():
        print('[loader] Dataset not found. Downloading...')

        try:
            from I7.server.download import download_data

            download_data()
        except Exception as e:
            print('[loader] Download failed:', e)
            return
    
    else:
        print('[loader] Dataset already exists.')
        
# Stream JSON
def stream_cards():
    
    ensure_dataset()
    
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        for card in ijson.items(f, 'item'):
            yield card
    
if __name__ == '__main__':
    stream_cards()