list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    test=False
    for j in list1:
        if j==1:
            continue
        if i==1:
            print("Number 1 is neither prime nor composite")
            break
        if i==j:
            continue
        if i%j==0:
            print(f"Number {i} is not prime number")
            break
        else:
            test=True
    if test==True:
        print (f"Number {i} is Prime number")
        
