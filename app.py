import os
import json
from time import sleep
from datetime import timezone
from dateutil.rrule import HOURLY, rrule
from dateutil.parser import parse
import pandas as pandas
from algosdk.v2client import indexer

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

indexerToken = os.environ.get('PURESTAKE_API_KEY')
myindexer = indexer.IndexerClient(indexer_token=indexerToken, indexer_address='https://testnet-algorand.api.purestake.io/idx2')

def get_txn_response(start_time, end_time, asset_id):
	"""
	Returns all transactions between start_time and end_time for any asset_id
	"""
	start_time = start_time.astimezone(timezone.utc).isoformat('T')
	end_time = end_time.astimezone(timezone.utc).isoformat('T')

	nexttoken = ''
	numtx = 1

	responses = []

	while numtx > 0:
		response = myindexer.search_transactions(start_time=start_time, end_time=end_time, asset_id=asset_id, limit=1000)
		transactions = response['transactions']
		responses += transactions
		numtx = len(transactions)
		if numtx > 0:
			nexttoken = response['next-token']
	return responses