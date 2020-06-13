from collections import Counter
n=int(input())
ara = list(map(int,input().split(",")))
l = dict(Counter(ara))
print(l)
l=dict(sorted(l.items(), key=lambda x: x[1]))
print(l.values())
ll=[]
for i ,j in l.items():
    print(i,j)
    if n!=0:
        n-=j
        ll.append(i)
    if n==0:
        break
#print(ll)
c=0
for i in set(ara):
    if i not in ll:
        c+=1
print(c)
