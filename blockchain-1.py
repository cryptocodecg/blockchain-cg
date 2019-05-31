#let's create a list of blockchain
blockchain = []

#now creating a function to add elements to the list
def add_list(b):
   #add element to the list using append
   blockchain.append(b)
   print(blockchain) #printing the list


#now let's add something to the list
add_list('A - B, 10') #we pretend that we are making notes
#of a transaction between A and B for 10 bitcoins :)
add_list('B - C, 2')
add_list('C - A, 1')
