#((p->q)^(q->r))->(p->r) TAUTOLOGY
'''values=[True,False]
results=[]
def implies(p,q):
    return not p or q

print("p\t q\t r\t result")
print("-"*32)
for p in values:
    for q in values:
        for r in values:
            a=implies(p,q)
            b=implies(q,r)
            c=implies(p,r)
            d=a and b
            result=implies(d,c)
            results.append(result)
            print(f"{p}\t{q}\t{r}\t{result}")
print("\nConclusion:")
if all(results):
    print("it is a tautology")
elif not any(results):
    print("it is contradiction")
else:
    print("it is contingency")
'''
#(p->q)^(p->r) CONTINGENCY
values=[True,False]
results=[]
def implies(p,q):
    return not p or q
print("p\t q\t r\t result")
print("-"*30)
for p in values:
    for q in values:
        for r in values:
            a=implies(p,q)
            b=implies(p,r)
            result=a and b
            results.append(result)
            print(f"{p}\t{q}\t{r}\t{result}")
print("\nConclusion:")
if all(results):
    print("it is a tautology")
elif not any(results):
    print("it is contradiction")
else:
    print("it is contingency")

#(p->q)^p^~q CONTRADICTION
values=[True, False]
results=[]
def implies(p,q):
    return not p or q
def negation(q):
    return not q
print("p\t q\t result")
print("-"*30)
for p in values:
    for q in values:
        a=implies(p,q)
        b=negation(q)
        c=p
        result=a and c and b
        results.append(result)
        print(f"{p}\t{q}\t{result}")
if all(results):
    print("tautology")
elif not any(results):
    print("contradiction")
else:
    print("contingency")