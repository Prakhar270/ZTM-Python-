from collections import Counter, OrderedDict, defaultdict

li = [1, 2, 3, 4, 5, 6, 7, 3, 7, 4, 7]
sentance = "blah blah blah thinking about python"

print(Counter(li))
print(Counter(sentance))
print("-------------------------")
dictionary = defaultdict(lambda: "Key doesn't exist", {'a' : 1, 'b' : 2})
print(dictionary['c'])
print("-------------------------")

d = OrderedDict()
d['a'] = 1
d['b'] = 2
'''
    if we take d = dict() then it give false because dict is unordered
'''
d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)