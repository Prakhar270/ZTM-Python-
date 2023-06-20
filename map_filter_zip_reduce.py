from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capital(items):
    return items.upper()

print(list(map(capital, my_pets)))
print(list(map(lambda m_pet : m_pet.upper() , my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(lambda my_score : my_score > 50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(my_numbers + scores)
print(reduce(lambda acc, items : acc + items , (my_numbers + scores), 0))

print("---------------------------------------------------------------------")

my_list = [5, 4, 3]
new_list = list(map(lambda num : num ** 2, my_list))
print(my_list)

a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x : x[1])
print(a) 