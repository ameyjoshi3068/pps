def prime_factors(num):
    list1=[1]
    for i in range(2,num):
        quotient=num/i
        remainder=num%i
        while remainder==0:
            list1.append(i)
            qu=quotient/i
            quotient=newNum%i
    if list1==[1]:
        list1.append(num)
    return list1

print(prime_factors(25))
