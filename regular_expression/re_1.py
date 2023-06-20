import re

string = 'search inside of this text please'

se = re.search('this', string)
print(se.span())
print(se.start())
print(se.end())
print(se.group())