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

    def check_arrows(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):

    def __init__(self, name, powers, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, powers)

hb1 = HybridBorg('borie', 50, 100)

print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())