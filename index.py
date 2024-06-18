
print(" ████  ███  █      ████ █   █ █      ███  █████  ███  ████  ")
print("█     █   █ █     █     █   █ █     █   █   █   █   █ █   █")
print("█     █████ █     █     █   █ █     █████   █   █   █ ████  ")
print("█     █   █ █     █     █   █ █     █   █   █   █   █ █   █ ")
print(" ████ █   █ █████  ████ █████ █████ █   █   █    ███  █   █ ")
print("")
print("")
print("")
x=int(input("enter the first value  :-  "))
y=input("enter the opration eg (+,-)  :-  ")
z=int(input("enter the second value  :-  "))
if y == '+':
    print("")
    print("")
    print("the answer is   ",x+z)
elif y == '-':
    print("")
    print("")
    print("the answer is   ",x-z)
elif y == '*':
    print("")
    print("")
    print("the answer is   ",x*z)
elif y == '/':
    print("")
    print("")
    print("the answer is   ",x/z)
elif y == 'x':
    print("")
    print("")
    print("the answer is   ",x*z)
else:
    print("sorry this opration is not valid. you are supposed to use +,-,/,x,*. ✮ツ")
print("")
print("")
print("")
print("thankyou for using the program ✮ツ")
s=input("type restart or end to restart or end the program respectively")
if s=="restart":
    print("Calculator")
    print("")
    print("")
    print("")
    x=int(input("enter the first value"))
    y=input("enter the opration eg:- (+,-)")
    z=int(input("enter the second value"))
    if y == '+':
         print("")
         print("")
         print("the answer is   ",x+z)
    elif y == '-':
         print("")
         print("")
         print("the answer is   ",x-z)
    elif y == '*':
         print("")
         print("")
         print("the answer is   ",x*z)
    elif y == '/':
         print("")
         print("")
         print("the answer is   ",x/z)
    elif y == 'x':
         print("")
         print("")
         print("the answer is   ",x*z)
    else:
         print("sorry this opration is not valid. you are supposed to use +,-,/,x,*")
         print("")
         print("")
         print("")
         print("thankyou for using the program")
else:
    print("thankyou")
