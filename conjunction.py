values=[True,False]
print("p \t q \t p^q")
for p in values:
    for q in values:
        print(f"{p}\t{q}\t{p and q}")
print()

print("p \t q \t p^q")
def con(p,q):
    return p and q

for p in [True,False]:
        for q in [True,False]:
            a=con(p,q)
            print(f"{p}\t{q}\t{a}")
