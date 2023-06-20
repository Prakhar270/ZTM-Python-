#Making own for loop
def special_for(iterable):
  iterator = iter(iterable)
  print("Self made for loop")
  while True:
    try:
      iterator
      print(next(iterator), end = " ")
    except StopIteration:
      break

#Making own range function
class MyGen:
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last
    MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(1,100)
print("Self made range()")
for i in gen:
    print(i, end = " ")
print()
gen2 = MyGen(1,50)
special_for(gen2)