import json
import hashlib


class MerkleTree(object):

    def __init__(self):
        self.root = None
        self.nodes = []  # Stores all other nodes except the leaf nodes
        self.leaves = []  # List of leaves of the tree. Leaves contain the transactions

    def add_node(self, node):
        # Add new node
        self.nodes.append(node)

    def add_leaf(self, leaf):
        # Add new leaf node
        self.leaves.append(leaf)


# You can use the classes for node and leaf or you can create your own.
'''
class MerkleTreeNode(object):

    def __init__(self):
        self.index = None
        self.parent = None
        self.child_left = None
        self.child_right = None
        self.hash = None


class MerkleTreeLeaf(object):

    def __init__(self):
        self.index = None
        self.parent = None
        self.transaction = None
        self.hash = None


def create_hashList(transactions):
    # Using the Merkle algorithm build the tree from a list of transactions in the block
    # transactions is list of Transaction
    hashList = []
    for t in transactions:
        hashList.append(hashlib.sha256(t).hexdigest())
    return hashList

def create_merkle_tree(hashList):
    if len(hashList) == 1:
        return hashList[0]

    newHashList = []

    for i in range(0, len(hashList) - 1, 2):
        newHashList.append(dhash256(hashList[i], hashList[i + 1]))

    if len(hashList) % 2 == 1:  # odd, hash last item twice
        newHashList.append(dhash256(hashList[-1], hashList[-1]))
    return create_merkle_tree(newHashList)

def dhash256(a, b):
    # due to big-endian / little-endian nonsense
    concat = a + b
    temp = hashlib.sha256(concat).digest()
    h = hashlib.sha256(temp).hexdigest()
    return h

'''






