__author__ = 'Norbert'

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay =  pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1 + percent)

bob = Worker('Robert Zielony', 50000)
anna = Worker('Anna Czerwony', 20000)
bobLastname = bob.lastName()
annLastname = anna.lastName()
print(bobLastname)
print(annLastname)
annSalary = anna.pay
print(annSalary)
anna.giveRaise(.10)
annSalary = anna.pay
print(annSalary)
