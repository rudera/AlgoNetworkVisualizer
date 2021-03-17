import os
import json
from time import sleep
from datetime import timezone
from dateutil.rrule import HOURLY, rrule
from dateutil.parser import parse
import pandas as pd
from algosdk.v2client import indexer

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

algod_address = "https://testnet-algorand.api.purestake.io/idx2"
algod_token = ""
headers = {
	"X-API-Key": os.environ.get('PURESTAKE_API_KEY')
}

myindexer = indexer.IndexerClient(algod_token, algod_address, headers)


def get_asset_txn(asset_id):
	 nexttoken = ""
	 numtx = 1
	 responses = []

	 while numtx > 0:
	 	response = myindexer.search_asset_transactions(asset_id = asset_id, next_page = nexttoken, limit-1000)
	 	transactions = response['transactions']
	 	responses += transactions
	 	numtx = len(transactions)
	 	if numtx > 0:
	 		nexttoken = response['next-token']
	 return responses


