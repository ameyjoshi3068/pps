num=int(input())
test=True
for i in range(num):
    if i==0 or i==1:
        continue
    if num%i==0:
        test=False
        print("Vibhav")
        break
if test:
    print("Omkar")