class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = weight / height

    def introduce_bmi(self):
        print(f'Hello my name is {self.name}, and my bmi is {self.bmi} .')

p1 = Person("Julian", 1.7, 72 )
p2 = Person("Min", 1.65, 53 )
p3 = Person("Waffa_boy", 1.8, 78)

p1.introduce_bmi()
p2.introduce_bmi()
p3.introduce_bmi()