import json

from block_header import BlockHeader
from transaction import Transaction
from block import Block
from blockchain import Blockchain


def read_header(header):
    # Implement these functions to help you
    # Takes a dictionary as an input
    return BlockHeader(header["index"], header["previous_hash"], header["timestamp"], header["nonce"])

def read_transaction(transaction):
    # Same above for transformation
    return Transaction(transaction["index"],transaction["sender"],transaction["receiver"],transaction["amount"])

def read_block(block):
    # Reads a block from a dictionary
    header = read_header(block["header"])
    transactions = []
    for t in block["transactions"]:
        transactions.append(read_transaction(t))
    return Block(header, transactions)

def read_block_json(block_json):
    # Reads a block in json format
    return read_block(json.loads(open(block_json, 'r').read()))

def read_chain(chain):
    # read the chain from a json str
    # Returns a list of Block
    # This method does not do any checking
    blocks = []
    for block in json.loads(chain):
        blocks.append(read_block(block))
    return blocks

'''       
for i in range (10):
    file = "blocks_to_prove/block" + str(i) + ".json"
    with open(file, 'r') as load_f:
        block = read_block(json.load(load_f))
        print("For file" + file +": ")


for i in range(0,10):
    block_chain = Blockchain()
    file = "blockchain_wallets/chain" + str(i) + ".json"
    with open(file,'r') as load_f:
        for block in read_chain(load_f.read()):
            block_chain.add_block(block)
        print("For " + file + " :")
        for (k,v) in block_chain.wallets.items():
           print(k + ": " + str(v))
        print("")
'''
        
for i in range(0,10):
     file = "blockchain_incorrect/chain" + str(i) + ".json"
     with open(file,'r') as load_f:
         block_chain = Blockchain()
         index_error = 0
         print("For " + file + " :")
         for block in read_chain(load_f.read()):
             if not block_chain.add_block(block):
                 print(" of the block " + str(index_error))
                 break
             else:
                 index_error += 1