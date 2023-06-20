def highist_even(li):
    test = 0
    for value in li:
        if value % 2 == 0 and value > test:
            test = value
    return test

print(highist_even([10,2,3,4,8,11,50,55,66]))