import re

string = 'this search this inside of this text please'
pattern = re.compile('this')
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.group())
print(b)
print(c)
print(d)