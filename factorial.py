#factorial calculation
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
n=int(input("enter a number: "))
if n<0:
    print("factorial does not exist!")
else:
    print("factorial of",n,"is:",fact(n))
print()
for n in range(n):
  print("factorial of",n,"is: ",fact(n))