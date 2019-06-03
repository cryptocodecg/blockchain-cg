import hashlib
import json

genesis_block = {
   'previous_hash': '',
   'index': 0,
   'transaction': [],
   'nonce': 23
}

blockchain = [genesis_block]
open_transactions = []

def get_last_value():
   return(blockchain[-1])

def add_value(recipient, sender, amount=1.0):
   transaction = {'sender': sender,
   'recipient': recipient,
   'amount': amount}
   open_transactions.append(transaction)

def get_transaction_value():
   tx_sender = raw_input('Enter the sender: ')
   tx_recipient = raw_input('Enter the recipient of the transaction: ')
   tx_amount = float(input('Enter your transaction amount: '))
   return tx_recipient, tx_amount

def print_block():
   for block in blockchain:
       print("Here is your block")
       print(block)

def hash_block(block):
   return hashlib.sha256(json.dumps(block).encode()).hexdigest()

last_block = blockchain[-1]
print "last block: " , last_block
last_hash = hash_block(last_block)
print "last hash: ", last_hash

