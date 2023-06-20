def float_sum(*args):
    print(str(sum(args)).rstrip('.0'))

float_sum(0.3, 0.7) #➞ 1
float_sum(0.35, 0.75) #➞ 1.1
float_sum(1.234, 5.6789) #➞ 6.9129

""" Create a function hash_ops that:
1.Creates a sha256 hash from a list of strings.
2.Groups the hash, alphas first digits second.
3.Returns a new sha256 hash from the grouped string.
       (Check resources) """

import hashlib
def hash_ops(value):
    m = hashlib.sha256()
    for i in value:
        m.update(i.encode())
        new_string = m.hexdigest()
    print(new_string)
hash_ops(["string1", "string2", "string3"])
hash_ops(["quick", "brown", "fox"] )
hash_ops(["i", "am", "not", "a", "crook"])