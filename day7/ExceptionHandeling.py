# while True:
#     a = input("enter expression")
#     ans = eval(a)
#     print(ans)

#     ch = input("press y to continue")
#     if ch != 'y':
#         break

from turtle import pen


li = [1,2,34,56,34]

def Func(a,b):
    try:
        c = a//b
        print(li[c])
        print(c)
    
    except IndexError:
        print("Provide a legit index")

    except ZeroDivisionError:
        print("Division by zero is not possible")

    except Exception as e:
        print(e)

    else:
        print("Success")

    finally:
        print("Finally")

Func(20,0)