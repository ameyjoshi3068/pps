# cook your dish here
ip=input()
N=int(ip[0])
D=int(ip[2])
L=[]
count1=[]
for i in range(N):
    L[i]=int(input())
for i in (L):
    for j in (L):
        if (i-j)<=D:
            count1.append(i)
print(len(count1))