import requests
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# load .env creds
load_dotenv()

# API access creds
client_id = os.getenv('CX_ENGINE'),
client_secret = os.getenv('KEY')
# Check your env values are accessible to main.py
# print(client_id, client_secret)

# user inputs - ask user for keywords in the terminal on run
q = input("Write your keyword and press ENTER: ")
hq = input("OPTIONAL Write your second keyword OR press ENTER to search: ")

''' Function: call_api

This function queries the Google Custom Search API, retrieves the top 10 
search results, and saves them to a CSV file. It includes status_code check, 
timeout and automatically saves results to a folder called 'search_results
'''


def call_api():

    # URL to call info from API
    url = 'https://www.googleapis.com/customsearch/v1?'

# Adjust the parametres to control the results and search process - see docs in README.md
    params = {
        'key': client_secret,
        'cx': client_id,
        'q': q,  # query string
        'hq': hq,  # appends query terms to q with AND operator
        'c2coff': '1',  # disable Chinese
        # 'cr': 'countryUK', # restricts search results to documents from UK
        'exactTerms': '',
        'excludeTerms': '',
        # 'fileType':'', # see docs
        'filter': '1',  # enable duplication filtering
        'gl': 'countryUK',  # geolocation of end user
        # 'hl': 'EN', # sets user interface lanaguage
        # 'imgColourType': 'color', #grey, mono, trans (transparent bkgnd)
        # 'imgDominantColor' : 'black', # most colours plus 'teal', 'gray'
        # 'imgsize' : 'huge', # small to xxlarge plus icon
        # 'imgType' : 'photo', # face, lineart, stock, clipart, animated
        'num': '10',  # number of search results to return - 1 min 10 max
        # 'rights':'cc_publicdomain', #licensing filter
        'safe': 'active',  # search safety level
        # 'searchType': 'image', # uncomment to search images
        # 'siteSearch' : '', # search a specific site
        # 'siteSearchFilter' : 'i', # e to turn off above
        'sort': 'date',  # sort by date
        # index page of first result to return (up to 100 results)
        'start': '1',
    }

# calling the API
    api_data = requests.get(url, params=params, timeout=2)
    print(f"Status code is:", api_data.status_code)
    data = api_data.json()
    # print the API JSON response to the terminal
    print(data)

# create and name the csv output file
    td = f'{datetime.now():%Y-%m-%d_%H-%M-%S}'
    df = pd.DataFrame(data["items"])
    directory = 'search_results'
    filename = f'{td}_{q}+{hq}_records_{client_id}.csv'
    csv_file_path = os.path.join(directory, filename)
    # Ensure the directory exists to save the file to
    if not os.path.exists(directory):
        os.makedirs(directory)
    # save the API response data in to a csv file
    df.to_csv(csv_file_path, index=False)
    print(f"Data has been written to {csv_file_path}")


# call the function to run the code
call_api()
