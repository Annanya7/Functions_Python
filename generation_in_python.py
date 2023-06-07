def mygen(p,q):
  sum,sub,div,mult,rem=p+q,p-q,p//q,p*q,p%q
  yield sum
  yield sub
  yield div
  yield mult
  yield rem

a,b=[int(x) for x in input("Enter the values").split(",")]
g=mygen(a,b)
print("The sum=",next(g))
print("The substraction=",next(g))
print("The division=",next(g))
print("The multiplication=",next(g))
print("The remainder=",next(g))
