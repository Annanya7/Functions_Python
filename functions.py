def disp(p,q,fun):
  print(fun(p,q))
def add(a,b):
  sum=a+b
  return sum
def subs(a,b):
  sub=a-b
  return sub
def mult(a,b):
  mul=a*b
  return mul
def div(a,b):
  d=a//b
  return d
def rem(a,b):
  r=a%b
  return r
choice,x,y=input("Enter your choice"),int(input("Enter x")),int(input("Enter y"))
print("The choice we entered={}".format(choice))
if choice=='+':
  print("The sum program")
  disp(x,y,add)
elif choice=='-':
  print("The substraction")
  disp(x,y,subs)
elif choice=='*':
  print("The multiplication")
  disp(x,y,mult)
elif choice=='//':
  print("The division")
  disp(x,y,div)
elif choice=='%':
  print("The remainder")
  disp(x,y,rem)
else:
  print("Invalid")
