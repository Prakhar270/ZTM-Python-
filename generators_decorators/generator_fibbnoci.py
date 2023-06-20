# Here is an example generator which calculates fibonacci numbers:
# generator version
def fib(number):
    a =  0
    b = 1
    for _ in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(21):
    print(x, end = " ")
print()


def fib2(number):
    a =  0
    b = 1
    result = []
    for _ in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(21))