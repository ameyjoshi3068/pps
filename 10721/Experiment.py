def prime_factors(num):
    list=[1]
    for i in range(2,num):
        quotient=num%i
        while quotient==0:
            quotient=num%i
            list.append(i)
        else:
            list.append(i)
    list.append
    return list

print(prime_factors(2))
