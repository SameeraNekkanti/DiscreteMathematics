values=[True,False]
print("p\t q\t p=>q")
for p in values:
    for q in values:
        print(f"{p}\t{q}\t{not p or q}")