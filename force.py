import itertools
n=int(raw_input("enter the no  of particle:"))
tu=()
li=[]
for i in range(n):
    tu=tuple(raw_input())
    li.append(tu)

li=[tuple(itertools.ifilter(str.strip, t)) for t in li]
input= [map(int, x) for x in li]

#function for calculation of attraction force bw two particle pA and pB
force=0
def aForce(pA,pB):
    Force=abs(input[pA][1]-input[pB][1])* max(input[pA][0],input[pB][0])
    return Force
#pairs
pairs=list(itertools.combinations(range(n),2))

#calculation fo total attraction force
ans=0
for pair in pairs:
    ans+=aForce(pair[0],pair[1])

print("totao force: %d ",ans)

