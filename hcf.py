def hcf(max,min):
    if(min==0):
        return max
    else:
        return hcf(min,max%min)
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a<b:
    min=a
    max=b
else:
    min=b
    max=a
print("the gcd of",a,"and",b,"is :",end="")
print(hcf(max,min))