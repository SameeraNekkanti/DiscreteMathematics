#9,10

values=[True,False]
def disjunction(p,q):
    return p or q
def conjunction(p,q):
    return p and q
def implication(p,q):
    return not p or q
print("p\tq\t r\t pVq \t p=>r\t qVr \t  (pVq)^(p=>r)\t full")

listq=[]
for p in values:
    for q in values:
        for r in values:
            a=disjunction(p,q)
            b=implication(p,r)
            c=disjunction(q,r)
            d=conjunction(a,b)
            e=implication(d,c)
            print(p,q,r,a,b,c,d,sep="\t")
            listq.append(e)
if False not in listq:
    print("tautology")
else:
    print("not tautology")