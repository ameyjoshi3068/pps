def prime_factors(num):
    list1=[1]
    for i in range(2,num):
        quotient=num%i
        while quotient==0:
            list1.append(i)
            newNum=quotient/i
            quotient=newNum%i
    if list1==[1]:
        list1.append(num)
    return list1

print(prime_factors(25))
