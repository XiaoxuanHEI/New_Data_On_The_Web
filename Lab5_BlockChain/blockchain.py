class Blockchain(object):

    def __init__(self):
        self.chain = [] # contains the blockchain
        self.wallets = dict() # Contains the amount of coin each user owns
        self.wallets["admin"] = 100000000000000

    def add_block(self, block):
        # Add a block to the chain
        # It needs to check if a block is correct
        # Returns True if the block was added, False otherwise
        if block.is_proof_ready() and self.check_legal_transactions(block):
            self.chain.append(block)
            self.update_wallet(block)
            return True
        else:
            return False

    def update_wallet(self, block):
        # Update the values in the wallet
        # We assume the block is correct
        for t in block.transactions:
            if t.receiver in self.wallets:
                self.wallets[t.receiver] += t.amount
            else:
                self.wallets[t.receiver] = t.amount
            if t.sender in self.wallets:
                self.wallets[t.sender] -= t.amount 

    def check_legal_transactions(self, block):
        # Check if the transactions of a block are legal given the current state
        # of the chain and the wallet
        # Returns a boolean
        is_first = True
        for t in block.transactions:
            if t.sender not in self.wallets:
                if is_first:
                    print("The index of the first incorrect is: " + str(t.index), end = "")
                    is_first = False
                return False
            elif (self.wallets[t.sender] < t.amount):
                if is_first:
                    print("The index of the first incorrect is in the transaction " + str(t.index), end = "")
                    is_first = False
                return False
        return True

