class SuperList(list):
    
    def __len__(self):
        return 1000

superlist1 = SuperList()
print(len(superlist1))
superlist1.append(5)
superlist1.append(7)
print(superlist1[:])

print(issubclass(SuperList, list))

print(issubclass(list, object))