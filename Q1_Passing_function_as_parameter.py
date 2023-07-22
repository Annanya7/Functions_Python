def disp(res):
    print(res)
def add(a,b):
    s=a+b
    return s

def mult(a,b):
    s=a*b
    return s

def div(a,b):
    s=a//b
    return s
ch,x,y=input("Enter choice"),int(input()),int(input())
if ch=='+':
    print("The addition")
    disp(add(x,y))
elif ch=='*':
    print("The multiplication")
    disp(mult(x,y))
elif ch=='/':
    print("The division")
    disp(div(x,y))
else:
    print("wrong choice")
