# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        print(*args[0])
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1) 

acha = {
    'Name' : 'Prakhar',
    'Age' : 18
}
a, *args = 1, acha 
print(args)