class PlayerCharacters:
    #Class object attribute
    membership = True
    #Creating private members
    __new_membership = None

    def __init__(self, name, age):
        self.name = name #Attributes
        self.age = age

    def run(self):
        #print("hey")
        return "done"

    def shout(self, umar, name):
        return f"hello {name} , your age is {umar}"

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def subtracting_things(cls, num, num3):
        return cls("Tommy", num - num3)

    #Making a method simillar to adding things
    @staticmethod #same as @classmethod but doesn't have cls parameters
    def adding_things2(num1, num2):
        return num1 + num2

if __name__ == '__main__':
    player1 = PlayerCharacters('Sindy', 44)
    player2 = PlayerCharacters('Andy', 21)
    
    print(player1.name, player1.age)
    print(player2.name, player2.age)
    
    print(player1.run())
    print(player1.shout(name = "Prakhar", umar = 19))
    print(player2.shout(umar = 34, name = " "))
    
    print(PlayerCharacters.adding_things(2, 3))
    player3 = PlayerCharacters.subtracting_things(55, 44) #initialise object
    print(player3.name, player3.age) #calling name and age of the player
    print(PlayerCharacters.adding_things2(3,4)) #calling method adding_things2
    #using private members
    print(player1._PlayerCharacters__new_membership)

    