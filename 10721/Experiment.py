def prime_factors(num):
    list=[]
    for i in range(2,num):
        quotient=num%i
        if quotient==0:
            list.append(i)
            

