"""
Web Scraping - Beautiful Soup
"""

# Importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
import xlsxwriter

# Target URL to scrap
url = "https://chaldal.com/tools-hardware"
# Headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

# Send request to download the data
response = requests.request("Get", url, headers=headers)

# Parse the downloaded data
data = BeautifulSoup(response.text, 'html.parser')

# Find all the sections with specified class name
cards_data = data.find_all('div', attrs={'class', 'product'})

# Total number of cards
print('Total Number of Cards Found: ', len(cards_data))

# Create a list to store the data
scraped_data = []
product_id = 4400
# Source code of hotel cards
for card in cards_data:
    # Initialize the dictionary
    card_details = {}

    product_id += 1 

    total_products = randint(5, 200)

    product_type = "Tools & Hardware"

    # Get the product name
    product_name = card.find('div', attrs={'class':'name'})

    # Get the product price
    product_price = card.find('div', attrs={'class': 'price'})
    
    # Get the product quantity
    product_quantity = card.find('div', attrs={'class':'subText'})

    print(product_id, product_name.text, product_type, product_quantity.text, product_price.text, total_products)

    # Add data to the dictionary
    card_details['product_id'] = product_id
    card_details['product_name'] = product_name.text
    card_details['product_type'] = product_type
    card_details['product_quanity'] = product_quantity.text
    card_details['product_price'] = product_price.text
    card_details['total_products'] = total_products 

    # Append the scraped data to the list
    scraped_data.append(card_details)
  
# Create a data frame from the list of dictionaries
dataFrame = pd.DataFrame.from_dict(scraped_data)

# Save the scraped data as CSV file
dataFrame.to_csv('44_Tools & Hardware.csv', index=False)  
