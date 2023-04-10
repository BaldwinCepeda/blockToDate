import os
import datetime
from dotenv import load_dotenv
from web3 import Web3

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables as usual
secret_key = os.getenv('SECRET_KEY')


# Connect to the Ethereum node over WebSocket
w3 = Web3(Web3.WebsocketProvider(
    secret_key))
# Testing connection by getting latest block
block = w3.eth.get_block('latest')
# get Latest block number
block_number = block['number']
print("The current block number is: ", block_number)


timestamp = w3.eth.get_block(block_number).timestamp

# Convert the timestamp to a date
date = datetime.datetime.fromtimestamp(timestamp)

print("The date of block: ", block_number , " Trasnlated to date is: " , date)
print("END OF SCRIPT")
