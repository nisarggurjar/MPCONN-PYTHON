from functools import reduce

li = [2,4,56,7,67,345,43,65]

ans = list(map(lambda num: num**3,li))
print(ans)

even_ele = list(filter(lambda x : x%2==0, li))
print(even_ele)


def add(a,b):
    return a+b

print(reduce(add, li))