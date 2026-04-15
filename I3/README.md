# Scryfall Data Curation Pipeline

This notebook allows someone to download and filter the `bulk-card` data from the Scryfall API. It includes a pipeline to clean and normalize the data for more efficient querying, and also a query language translator to allow the user to query the dataset within the notebook in a way that matches Scryfall's query syntax, while leveraging pandas Dataframe methods. This data can then be saved to a CSV file for portability and further analysis.

## Tech Stack and Usage Guide
The notebook is written entirely in python, using several popular libraries such as `pandas`, and leverages Scryfall's REST-like API for fetching card data.  
Simply open the notebook in your environment of choice (can run `jupyter notebook` in a terminal if you have Jupyter installed on your system) and click Run All cells.  
The query may be be modified using terminology from Scryfall's query language. For example, this query: `f'set:{set_code} type:creature order:cmc'` will return all creatures from a certain set, ordered by cmc.
