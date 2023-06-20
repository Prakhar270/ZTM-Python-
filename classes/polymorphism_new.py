class User():
    
    def sign_in(self):
        print("Logged in")

    def attack(self):
        print("Do Nothing")

class Wizard(User):
    
    def __init__(self, name, powers):
        self.name = name
        self.powers = powers

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.powers}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

print("--------------------------")

for char in [wizard1, archer1]:
    char.attack()
