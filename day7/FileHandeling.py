# F = open(filename, mode)

# r: read
# w: write
# a: append
# r+: read and write with existing text
# w+: read and write (override)
# a+ : read + write (at end write)


# f = open('test.txt', 'r')

# # print(f.read())
# print(f.read(19))

# for l in f:
#     print(l)



# f = open('python.txt', 'w')
# f.write("Hello World")
# f.write("Python")
# f.close()

# f = open('python.txt', 'w')
# f.write("Python")
# f.write("Hello World")
# f.close()

# f = open("python.txt", "a")
# f.write("hello")
# f.close()
# f = open("python.txt", "a")
# f.write("hello")
# f.close()

f = open('python.txt', 'wb')
f.write()
f.close()