# cook your dish here
ip=input()
N=int(ip[0])
D=int(ip[3])
L=[]
count1=[]
ipcount=[]
for i in range(N):
    L[i]=int(input())
    ipcount.append(L[i])
for i in (ipcount):
    for j in (ipcount):
        if (i-j)<=D:
            count1.append(i)
print(len(count1))