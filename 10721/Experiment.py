def prime_factors(num):
    list1=[1]
    quotient=num
    for i in range(2,num):
        quotient=quotient/i
        remainder=quotient%i
        while remainder==0:
            list1.append(i)
            quotient=quotient/i
            remainder=quotient%i
    if list1==[1]:
        list1.append(num)
    return list1

print(prime_factors())
