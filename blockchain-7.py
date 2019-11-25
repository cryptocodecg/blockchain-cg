blockchain = []

def get_last_value():
   return(blockchain[-1])

def add_value(transaction_amount, last_transaction=[1]):
   blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
   tx_sender = input('Enter the sender: ') 
   tx_recipient = input('Enter the recipient of the transaction: ')
   tx_amount = float(input('Enter your transaction amount: '))
   return tx_sender, tx_recipient, tx_amount

def print_block():
   for block in blockchain:
       print("Here is your block")
       print(block)

def get_user_choice():
   user_input = input("Please give your choice here: ")
   return user_input

#this is the function for verifying the validity
#of the chain
#it will check the index and the content of each 
#block in the chain
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

tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
   print("Choose an option")
   print('Choose 1 for adding a new transaction')
   print('Choose 2 for printing the blockchain')
   print('Choose 3 if you want to manipulate the data')
   print('Choose anything else if you want to quit')

   user_choice = get_user_choice()

   if user_choice == '1':
       tx_amount = get_transaction_value()
       add_value(tx_amount, get_last_value())
   elif user_choice == '2':
       print_block()
   elif user_choice == '3':
#so when we want to modify the chain like this
#the function will refuse to make any changes
       if len(blockchain) >= 1:
           blockchain[0] = 2
   else:
       break

   if not verify_chain():
       print('Blockchain manipulated')
       break 
