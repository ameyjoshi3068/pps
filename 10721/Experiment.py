def prime_factors(num):
    list=[]
    for i in range(2,num):
        quotient=num%i
        while quotient==0:
            quotient=num%i
            list.append(i)


