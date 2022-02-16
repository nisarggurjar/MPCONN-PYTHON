li = [1,24,435,56,5]
print(li)
# li.insert(2,76)
# print(li)

# Insert(list, pos, ele)

# def Insert(li, pos, ele):
#     temp = list() # temp = []
#     for i in range(len(li)):
#         if i==pos:
#             temp.append(ele)
#             temp.append(li[i])
#         else:
#             temp.append(li[i])
#     return temp


def Insert(li, pos, ele):
    
    temp = li[:pos] + [ele] + li[pos:]
    return temp

a = Insert(li, 2, 72)
print(a)