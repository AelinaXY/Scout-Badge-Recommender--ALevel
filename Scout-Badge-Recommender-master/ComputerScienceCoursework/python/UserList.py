class User:


    tricks = []             # Global Variable to all instance Objects

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
