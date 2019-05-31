#import json

blockchain = []

def get_last_value():
   return(blockchain[-1])

def add_value(sender, recipient, amount=1.0):
   transaction = {'sender': sender,
   'recipient': recipient,
   'amount': amount}
   blockchain.append(transaction)

def get_transaction_value():
   tx_sender = raw_input('Enter the sender: ') 
   tx_recipient = raw_input('Enter the recipient of the transaction: ')
   tx_amount = float(raw_input('Enter your transaction amount: '))
   return tx_sender, tx_recipient, tx_amount

def print_block():
   for block in blockchain:
       print("Here is your block")
       print(block)

again = True
while again == True:
   tx = get_transaction_value()
   s, r, a = tx
   add_value(s, r, a)
   print(blockchain)
   more = raw_input("add more block (Y/N)? ")
   if more.lower() == 'y':
      again = True
   else:
      again = False
   
