import json
import hashlib
#from merkle_tree import create_merkle_tree, create_hashList


class Block(object):

    def __init__(self, header, transactions):
        # Store everything internally
        # header is a BlockHeader and transactions is a list of Transaction
        # call create_merkle_tree function to store transactions in Merkle tree
        self.N_STARTING_ZEROS = 4
        self.header = header
        self.transactions = transactions
        # create_merkle_tree(create_hashList(transactions))

    def to_dict(self):
        # Turns the object into a dictionary
        # There are two fields: header and transactions
        # The values are obtained by using the to_dict methods
        block_dict = {}
        block_dict['header'] = self.header
        block_dict['transactions'] = self.transactions
        return block_dict

    def to_json(self):
        # Transforms into a json string
        # use the option sort_key=True to make the representation unique
        return json.dumps(self.to_dict(), sort_key=True)

    def is_proof_ready(self):
        # Check whether the block is proven
        # For that, make sure the hash begins by N_STARTING_ZEROS
        hash_value = self.header.get_hash()
        if hash_value[:self.N_STARTING_ZEROS] == "0000":
            return True
        else:
            return False

    def make_proof_ready(self):
        # Transforms the block into a proven block
        nonce = 0
        while not self.is_proof_ready():
            nonce += 1
            self.header.set_nonce(nonce)
        print("nonce: " + str(nonce))
        print("hash value: " + self.header.get_hash())
        print("")

