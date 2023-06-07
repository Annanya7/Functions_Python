def da(basic):
    da=0.8*basic
    return da
def hra(basic):
    hra=0.15*basic
    return hra
def pf(basic):
    pf=0.12*basic
    return pf
b=int(input("Enter the basic salary"))
gross=b+da(b)+hra(b)
inc_tax=0.1*gross
net=gross-pf(b)-inc_tax
print("The net salary",net)

