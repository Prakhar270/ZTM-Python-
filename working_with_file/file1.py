my_file = open(r'F:\extra work\ZTM(PYTHON)\working_with_file\test.txt')

#print(my_file)
print(my_file.read())
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())

my_file.close()