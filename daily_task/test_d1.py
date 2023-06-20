import hashlib

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def hash_ops(li):
  length = len(li)
  m = hashlib.sha256()
  for i in range(0,length):
    m.update(str.encode(li[i]))
  hash = m.hexdigest()
  
  hash_sorted = sorted(hash)
  hash_sorted_num = []
  hash_sorted_str = []
  for item in hash_sorted:
    if RepresentsInt(item) == False:
      hash_sorted_str.append(item)
    else:
      hash_sorted_num.append(item)
  grouped_hash = "".join(hash_sorted_str)+ "".join(hash_sorted_num)
  n = hashlib.sha256(str.encode(grouped_hash)).hexdigest()
  return n

print(hash_ops(["string1", "string2", "string3"]))
print(hash_ops(["quick", "brown", "fox"]))
print(hash_ops(["i", "am", "not", "a", "crook"]))