li = [1,34,54,3,43,23,5,65,1,34,3,43,34,5,65,34,1,54]

# def Index(li, ele):
#     c = 0
#     for i in li:
#         if i == ele:
#             return c
#         c+=1

# a = Index(li, 0)
# print(a)



def Count(li, ele):
    c = 0
    for i in li:
        if i == ele:
            c+=1
    return c
        

a = Count(li, 54)
print(a)