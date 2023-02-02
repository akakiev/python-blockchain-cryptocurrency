#Diving into the basics of Python

blockchain = [[1]]

def add_value():
    #function that appends values
    blockchain.append([blockchain[-1], 5.3])
    print(blockchain)

for i in range (5):
    add_value()
