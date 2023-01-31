def prime_factors(num):
    list1=[]
    quotient=num
    for i in range(2,num):
        remainder=quotient%i
        while remainder==0:
            list1.append(i)
            quotient=quotient/i
            remainder=quotient%i
    if list1==[]:
        list1.append(num)
    return map(str,list1)

print("The prime factors of the number ="," X ".join(prime_factors(1024)))