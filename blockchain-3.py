genesis_block = {
   'previous_hash': '',
   'index': 0,
   'transaction': [],
   'nonce': 23
}

blockchain = [genesis_block]

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
   return tx_sender, tx_recipient, tx_amount

def get_user_choice():
   user_input = input("Please give your choice here: ")
   return user_input

def print_block():
   for block in blockchain:
       print("Here is your block")
       print(block)

print_block()
'''
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

while True:
   print("Choose an option")
   print('Choose 1 for adding a new transaction')
   print('Choose 2 for mining a new block')
   print('Choose 3 for printing the blockchain')
   print('Choose anything else if you want to quit')

   user_choice = get_user_choice()
   
   if user_choice == 1:
       tx_data = get_transaction_value()
       recipient, amount = tx_data
       add_value(recipient, amount=amount)
       print(open_transactions)
   elif user_choice == 2:
       mine_block()
   elif user_choice == 3:
       print_block()
   else:
       break
'''
