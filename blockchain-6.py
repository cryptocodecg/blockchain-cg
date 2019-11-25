import hashlib
import json

#the reward for the miner
reward = 10.0

genesis_block = {
   'previous_hash': '',
   'index': 0,
   'transaction': [],
   'nonce': 23
}

blockchain = [genesis_block]
#list of transactions
open_transactions = []
#the owner of the blockchain
owner = 'procodecg'

def get_last_value():
   return(blockchain[-1])

def add_value(recipient, sender=owner, amount=1.0):
   transaction = {'sender': sender,
   'recipient': recipient,
   'amount': amount}
   open_transactions.append(transaction)

def get_transaction_value():
   tx_recipient = input('Enter the recipient of the transaction: ')
   tx_amount = float(input('Enter your transaction amount: '))
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

#we have learned about all the functions above
#now we will see the last function that will do mining 
#process
def mine_block():
#get the last block
   last_block = blockchain[-1]
#hash the last block
   hashed_block = hash_block(last_block)
#find the nonce
   nonce = pow()
#give reward for the miner
   reward_transaction = {
           'sender': 'MINING',
           'recipient': owner,
           'amount': reward
       }
#add the transaction to the list of transaction
   open_transactions.append(reward_transaction)
   block = {
       'previous_hash': hashed_block,
       'index': len(blockchain),
       'transaction': open_transactions,
       'nonce': nonce
   }
#add the block to the blockchain
   blockchain.append(block)

#we will learn about verifying the chain
#in the next tutorial
def verify_chain():
   index = 0
   valid = True
   for block in blockchain:
       if index == 0:
           index += 1
           continue
       elif block[0] == blockchain[index - 1]:
           valid = True
       else:
           valid = False
           break
       index += 1
   return valid

#the looping for the user to enter the choice
#we choose 1 to add new transaction
#then 2 to mine a new block
#then 3 to print the blockchain
while True:
   print("Choose an option")
   print('Choose 1 for adding a new transaction')
   print('Choose 2 for mining a new block')
   print('Choose 3 for printing the blockchain')
   print('Choose anything else if you want to quit')

   user_choice = get_user_choice()
   
   if user_choice == '1':
       tx_data = get_transaction_value()
       recipient, amount = tx_data
       add_value(recipient, amount=amount)
       print(open_transactions)
   elif user_choice == '2':
       mine_block()
   elif user_choice == '3':
       print_block()
   else:
       break
