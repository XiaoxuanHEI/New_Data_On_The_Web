class Transaction(object):

    def __init__(self, index, sender, receiver, amount):
        # Store internally
        self.index = index
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_dict(self):
        # Transform object into a dictionary for future transformation in JSON
        # The names of the fields are the name of the variables
        tran_dict = {}
        tran_dict["index"] = self.index
        tran_dict["sender"] = self.sender
        tran_dict["receiver"] = self.receiver
        tran_dict["amount"] = self.amount
        return tran_dict