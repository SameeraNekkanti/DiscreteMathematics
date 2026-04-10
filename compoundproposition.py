#(pv~q)->p^q
results=[]
def disjunction(p,q):
    return p or q
def conjunction(p,q):
    return p and q
def implication(p,q):
    return not p or q
print("p\t q\t ~q\t pv~q\t p^q\t (pv~q)=> p^q")
values=[True,False]
for p in values:
    for q in values:
        a=not q
        b=disjunction(p,a)
        c=conjunction(p,q)
        d=implication(b,c)
        print(f"{p}\t {q}\t {a}\t {b}\t {c}\t {d}")
        results.append(d)
if all(results):
    print("tautology")
elif not any(results):
    print("contradiction")
else:
    print("contingency")

#((p->q)^(q->r)->(p->r))
def implication(p,q):
    return not p or q
def conjunction(p,q):
    return p and q
print("p\tq\tr\tp->q\tq->r\tp->r\tresult")
values=[True,False]
for p in values:
    for q in values:
        for r in values:
            a=implication(p,q)
            b=implication(q,r)
            c=implication(p,r)
            d=conjunction(a,b)
            result=implication(d,c)
            print(f"{p}\t{q}\t{r}\t{a}\t{b}\t{c}\t{d}")

#~(pvq)<=>(~p^~q)
values=[True, False]
def disjunction(p,q):
    return p or q
def negation(p):
    return not p
def conjunction(p,q):
    return p and q
def biderectional(p,q):
    return (not p or q) and (not q or p)
print("p\tq\t~(pvq)\tresult")
for p in values:
    for q in values:
        a=disjunction(p,q)
        b=negation(a)
        c=negation(p)
        d=negation(q)
        e=conjunction(c,d)
        f=biderectional(b,e)
        print(f"{p}\t{q}\t{b}\t{f}")

#(p^q)^(q->r)v(p->r)
values=[True,False]
results=[]
def conjunction(p,q):
    return p and q
def implication(q,r):
    return not q or r
def disjunction(p,q):
    return p or q
print("p\tq\tr\tresult")
for p in values:
    for q in values:
        for r in values:
            a=conjunction(p,q)
            b=implication(q,r)
            c=implication(p,r)
            result=conjunction(a,d)
            d=disjunction(b,c)
            results.append(result)
            print(f"{p}\t{q}\t{r}\t{result}")
if all(results):
    print("tautology")
elif not any(results):
    print("contradiction")
else:
    print("contingency")
