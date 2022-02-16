li = [0,1,2,3,4,5]

def POP(li, pos = -1):
    ele = li[pos]
    temp = list()
    for i in range(len(li)):
        if i == pos:
            continue
        temp.append(li[i])
    return ele


# a = POP(li, 3)
# print(a)

def add(*iter):
    s = 0
    for i in iter:
        s+=i
    print(s)

# add(14,14,34,345,345,34,6,234,234,56)

def Func(**kwargs):
    print(kwargs)

Func(fn = 'nisarg', ln = 'gurjar')