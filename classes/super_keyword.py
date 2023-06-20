class User():

    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    
    def __init__(self, name, powers, email):
        super().__init__(email) # OR User.__init__(self, email)
        self.name = name
        self.powers = powers

    def attack(self):
        print(f'Attacking with power of {self.powers}')

class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email) # OR User.__init__(self, email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 60, 'Merlin@gmail.com')
archer1 = Archer('Robin', 30, 'Robin@gmail.com')

print(wizard1.email)

'''
 OBJECT INTROSPECTION
'''
print(dir(wizard1))