#[(pvq)^(7pvr)]->(qvr)
def disjunction(p,q):
    return p or q
def conjunction(p,q):
    return p and q
def implication(p,q):
    return not p or q
def negation(p):
    return not p
print("p\tq\tr\tpvq\t7pVr\tqvr\tresult")
values=[True,False]
results=[]
for p in values:
    for q in values:
        for r in values:
            a=disjunction(p,q)
            b=negation(p)
            c=disjunction(b,r)
            d=conjunction(a,c)
            e=disjunction(q,r)
            result=implication(d,e)
            results.append(result)
            print(f"{p}\t{q}\t{r}\t{a}\t{c}\t{e}\t{result}")
if all(results):
    print("tautology")
elif not any(results):
    print("contradiction")
else:
    print("contingency")