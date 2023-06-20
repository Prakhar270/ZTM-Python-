class User():
    
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    
    def __init__(self, name, powers):
        self.name = name
        self.powers = powers

    def attack(self):
        print(f'Attacking with power of {self.powers}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
print(wizard1.sign_in())
wizard1.attack()
archer1.attack()

print(f'wizard1 is instance of Wizard Class: {isinstance(wizard1, Wizard)}')
print(f'archer1 is instance of Archer Class: {isinstance(archer1, Archer)}')
print(f'wizard1 is instance of Archer Class: {isinstance(wizard1, Archer)}')
print(f'archer1 is instance of Wizard Class: {isinstance(archer1, Wizard)}')
print(f'wizard1 is instance of User Class: {isinstance(wizard1, User)}')
print(f'archer1 is instance of User Class: {isinstance(archer1, User)}')
print(isinstance(wizard1, object))
print(isinstance(archer1, object))

