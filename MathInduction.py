#2+4+6+...+2n=n*(n+1)

def LHS(n):
    return sum(range(2,2*n,2))

def RHS(n):
    return n*(n+1)

n=int(input("enter maximum number"))

#Base Case
print("\nBASE CASE (n=1):")
if LHS(1)==RHS(1):
    print("True")
else:
    print("False")

#Inductive Step Verification
print("\nINDUCTIVE STEP:")
for k in range(2,n):
    if LHS(k)==RHS(k) and LHS(k+1)==RHS(k+1):
        print(f"True for k = {k}=> True for k+1 = {k+1}")
    else:
        print(f"Failed at k = {k}")
        break