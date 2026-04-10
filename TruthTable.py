values=[True, False]
print("truth table")
def disjunction(p,q,):
    return p or q
def conjunction(p,q,r):
    return p and q and r
def implication(p, q):
    return not p or q
print("p\tq\t r\t pVq \t p=>r\t q=>r \t full")
print("p\t q \tr \ta\t b \tc \td ")
l=[]
for p in values:
    for q in values:
        for r in values:
            a=disjunction(p,q)
            b=implication(p,r)
            c=implication(q,r)
            d=implication(conjunction(a,b,c),r)
            print(p,q,r,a,b,c,d,sep="\t")
            l.append(d)

if False not in l:
            print("tautology")
else:
            print("not tautology")
