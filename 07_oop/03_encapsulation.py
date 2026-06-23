class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self.__balance = balance    # Private attribute

    # Getter method to safely access private data
    def get_balance(self):
        return self.__balance