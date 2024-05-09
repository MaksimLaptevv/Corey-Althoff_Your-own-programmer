class horse:
    def __init__(self,name):
        self.name=name

class human:
    def __init__(self,name,horse):
        self.name=name
        self.horse=horse

horse=horse('my little pony')
bill=human('Bill',horse)

print(bill.horse.name)