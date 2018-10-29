def foo(x, lst=[]):
    lst.append(x)
    return lst
  
print(foo(24))
print(foo(42))

def multipliers():
    return [lambda x: i * x for i in range(3)]
  
for multiplier in multipliers():
    print(multiplier(3))

lst = [1,2,3]

def add1():
    lst.append(4)
  
def add2():
    lst += [5]
  
add1()
print(lst)
add2()
print(lst)

# коллекция - бежим по ней - замыкание

# он коммит