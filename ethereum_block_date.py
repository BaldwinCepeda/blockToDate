import os
import datetime
from dotenv import load_dotenv
from web3 import Web3

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables as usual
secret_key = os.getenv('SECRET_KEY')

# Connect to an Ethereum node using web3.py
w3 = Web3(Web3.HTTPProvider(secret_key))

# Retrieve the timestamp of a block, keeping in mind that you can use any block number as per your requirement.
# The current block number mentioned here is only an example."
block_number = w3.eth.get_block_number()
timestamp = w3.eth.getBlock(block_number).timestamp

# Convert the timestamp to a date
date = datetime.datetime.fromtimestamp(timestamp)


# def date_to_block_number(date):
#     # Convert the given date to a Unix timestamp
#     timestamp = datetime.datetime.timestamp(date)

#     # Get the latest block number
#     latest_block = w3.eth.block_number

#     # Iterate over the blocks starting from the latest block
#     for i in range(latest_block, 0, -1):
#         # Get the timestamp of the current block
#         block_timestamp = w3.eth.getBlock(i).timestamp

#         # Check if the current block's timestamp is less than or equal to the given timestamp
#         if block_timestamp <= timestamp:
#             # If a block with a timestamp less than or equal to the given timestamp is found, return its number
#             return i

#     # If no block with a timestamp less than or equal to the given timestamp is found, return None
#     return None


# # now an example of the function
# # Random date
# # Create a datetime object representing January 1, 2022, at 00:00:00
# # constructor to create the object and pass in the year, month, day, hour, minute, and second as arguments.
# my_date = datetime.datetime(2022, 1, 1, 0, 0, 0)

# dateToBlock = date_to_block_number(my_date)


# Print the date
print("The date of the latest Ethereum block is:", date)

print("END OF PROGRAM")
