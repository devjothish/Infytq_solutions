from itertools import permutations
s = input()
ss = set()
m=-1
for i in s:
    if i.isdigit():
        ss.add(i)
print(ss)
p = list(permutations(ss,len(ss)))
print(p)
for i in p:
    k="".join(i)
    print(k)
    if int(k)%2==0 and int(k)>m:
        m=int(k)
        
print(m)
