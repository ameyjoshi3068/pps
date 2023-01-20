def prime_factors(num):
    list=[]
    for i in range(2,num):
        if num%i==0:
            list.append(i)
            
