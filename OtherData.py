# Importing required libraries
from random import randint
import random
from datetime import datetime, timedelta

min_year=2020
max_year=datetime.now().year

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+1
end = start + timedelta(days=365 * years)


# Create a list to store the data
scraped_data = []
payment_id = 55010100
payment_customer_id = 15010100

# Random text generator for payment status
verbs = ("paid", "due")

# Source code of hotel cards
for card in range(30):
    # Initialize the dictionary
    card_details = {}

    payment_id += 1

    payment_customer_id += 1

    payment_amount = randint(30, 5000)
    
    # Payment random date 
    payment_date = start + (end - start) * random.random()

    num = random.randrange(0, 2)

    print(payment_id, payment_customer_id, payment_amount, payment_date, verbs[num])

    # Add data to the dictionary
    card_details['payment_id'] = payment_id
    card_details['payment_customer_id'] = payment_customer_id
    card_details['payment_amount'] = payment_amount
    card_details['payment_date'] = payment_date
    card_details['payment_date'] = verbs[num]

    # Append the scraped data to the list
    scraped_data.append(card_details)
  
# Create a data frame from the list of dictionaries
# dataFrame = pd.DataFrame.from_dict(scraped_data)

# Save the scraped data as CSV file
# dataFrame.to_csv('44_Tools & Hardware.csv', index=False)  