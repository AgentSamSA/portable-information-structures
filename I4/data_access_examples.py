"""
Instructions to run:

1. Install dependencies:
   pip install requests pandas beautifulsoup4

2. Run:
   python data_access_examples.py

No API keys required.
"""

import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

# --------------------------------------------------
# 1. API ACCESS (JSON via HTTP)
# --------------------------------------------------
def fetch_scryfall_cards():
   """
   Access Method: API over HTTP
   Structure: JSON

   Pros:
   - Always up-to-date data
   - No need to store large datasets locally
   - Structured and easy to parse

   Cons:
   - Requires internet connection
   - Rate limits may apply
   - Slower than local access for large datasets
   """
   
   url = 'https://api.scryfall.com/bulk-data'
   res = requests.get(url)
   data = res.json()

   print('\n--- Scryfall API Sample ---')
   for card in data['data'][:5]:
      print(card['name'])

# --------------------------------------------------
# 2. LOCAL FILE ACCESS (CSV)
# --------------------------------------------------
def read_local_csv():
   """
   Access Method: Local file read
   Structure: CSV

   Pros:
   - Very fast access
   - Works offline
   - No API limits

   Cons:
   - Data can become outdated
   - Requires manual download/storage
   - Larger storage requirements
   """

   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   path = os.path.join(BASE_DIR, 'combined_csv_pts.csv')
   df = pd.read_csv(path)

   print('\n--- Local CSV Sample ---')
   print(df.head())

# --------------------------------------------------
# 3. HTML SCRAPING (WEB PAGE)
# --------------------------------------------------
def scrape_wikipedia():
   """
   Access Method: HTML over HTTP (web scraping)
   Structure: HTML

   Pros:
   - Access to data not available via API
   - Flexible for many websites

   Cons:
   - Fragile (website structure may change)
   - Slower and less reliable
   - May violate terms of service if abused
   """

   url = 'https://en.wikipedia.org/wiki/List_of_Magic:_The_Gathering_sets'
   res = requests.get(url)

   soup = BeautifulSoup(res.text, 'html.parser')

   print('\n--- Wikipedia Scrape Sample ---')

   # Get all list items
   items = soup.find_all('li')

   count = 0
   for item in items:
      text = item.get_text(strip=True)
      if text:
         print(text)
         count += 1
      if count >= 5:
         break

if __name__ == '__main__':
   fetch_scryfall_cards()
   read_local_csv()
   scrape_wikipedia()