s = input()
c=0
even = []
odd = []
for i in s:
    if i.isalnum():
        c+=1
    if i.isdigit():
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
print(c)
print(even)
print(odd)
if c%2==0:
    if len(even) > len(odd):
        t = len(odd)
        out = even
    else:
        t=len(even)
        out=odd
    for i in range(t):
        print("{}{}".format(even[i],odd[i]),end="")
    for j in out[t:]:
        print(j,end="")
else:
    if len(even) > len(odd):
        t = len(odd)
        out = even
    else:
        t=len(even)
        out = odd
    for i in range(t):
        print("{}{}".format(odd[i],even[i]),end="")
    for j in out[t:]:
        print(j,end="")
