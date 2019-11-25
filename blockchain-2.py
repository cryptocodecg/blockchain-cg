#defining the list/chain
blockchain = []

#getting the last value/transaction
def get_last_value():
   return(blockchain[-1])

#adding transaction
#now we have sender, recipient and amount
def add_value(sender, recipient, amount=1.0):
   transaction = {'sender': sender,
   'recipient': recipient,
   'amount': amount}
   blockchain.append(transaction)

#getting the details of transaction by entering to the prompt
def get_transaction_value():
   tx_sender = input('Enter the sender: ') 
   tx_recipient = input('Enter the recipient of the transaction: ')
   tx_amount = float(input('Enter your transaction amount: '))
   return tx_sender, tx_recipient, tx_amount

#printing the blockchain
def print_block():
   for block in blockchain:
       print("Here is your block")
       print(block)

#the code will keep repeating for more transaction
#until the user answer is no 
again = True
while again == True:
   tx = get_transaction_value()
   s, r, a = tx
   add_value(s, r, a)
   print(blockchain)
   more = input("add more block (Y/N)? ")
   if more.lower() == 'y':
      again = True
   else:
      again = False
   
