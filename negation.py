values=[True,False]
print("p\t ~p")
for p in values:
    print(f"{p}\t {not p}")
print()
#function
def neg(n):
    return not n
print("p\t 7p")
for p in [True,False]:
    print(f"{p}\t",neg(p))