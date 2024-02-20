#tuple

def fun():
    t1=(11,22,33,44,55)
    print(f"tuple t1={t1}  type of t1={type(t1)}")

    tstr=("pune","karad")
    print(f"tuple tstr={tstr}  type of tstr={type(tstr)}")

    t2=(55,"karad")
    print(f"tuple t2={t2}  type of t2={type(t2)}")

    print(f"first ele of tuple={t2[0]}")
    print(f"second ele of tuple={t2[1]}")

#fun()

n1,n2=11,22
print("before swap")
print(f"n1={n1}")
print(f"n2={n2}")

n1,n2=n2,n1
print("after swap")
print(f"n1={n1}")
print(f"n2={n2}")