#Diving into the basics of Python

blockchain = [1]

def add_value():
    blockchain.append([blockchain[0], 5.3])
    print(blockchain)

for i in range (4):
    add_value()
