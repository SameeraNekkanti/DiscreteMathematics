values=[True,False]
print("p \t q \t pVq \t p^q")
for p in values:
    for q in values:
        print(f"{p}\t{q}\t{p or q} \t{p and q}")

