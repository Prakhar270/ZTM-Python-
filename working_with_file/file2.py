with open(r'F:\extra work\ZTM(PYTHON)\working_with_file\test.txt') as my_file:
    print(my_file.readlines())

with open(r'F:\extra work\ZTM(PYTHON)\working_with_file\test.txt', mode = 'r+') as my_file:
    text = my_file.write('\n:)')
    print(my_file.readlines())