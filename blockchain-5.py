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
   tx_recipient = raw_input('Enter the recipient of the transaction: ')
   tx_amount = float(input('Enter your transaction amount '))
   return tx_recipient, tx_amount

def get_user_choice():
   user_input = input("Please give your choice here: ")
   return user_input

def print_block():
   for block in blockchain:
       print("Here is your block")
       print(block)

def hash_block(block):
   return hashlib.sha256(json.dumps(block).encode()).hexdigest()

def valid_proof(transactions, last_hash, nonce):
   guess = (str(transactions) + str(last_hash) + str(nonce)).encode()
   guess_hash = hashlib.sha256(guess).hexdigest()
   print(guess_hash)
   return guess_hash[0:2] == '00'

def pow():
   last_block = blockchain[-1]
   last_hash = hash_block(last_block)
   nonce = 0
   while not valid_proof(open_transactions, last_hash, nonce):
       nonce += 1
   return nonce

print blockchain 
nonce = pow()
print nonce
