sum=0
cnt=1
N = int(input())
for k in range(1,N+1):
    cnt*=k
    sum+=1/cnt
print(1+sum)