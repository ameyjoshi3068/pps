def prime_factors(num):
    list=[1]
    for i in range(2,num):
        quotient=num%i
        while quotient==0:
            list.append(i)
            quotient=quotient%i
    if list==[1]:
        list.append(num)
    return list

print(prime_factors(25))
