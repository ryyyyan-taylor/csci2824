def prime_factorization(n):
    res = []
    i = 2
    while (i <= n):
        isPrime = True
        for j in range(2, i):
            if (i % j == 0):
                isPrime = False
        if isPrime:
            count = 0
            while (n % i == 0 and isPrime):
                count += 1
                n = n // i
            res.append(count)
        i += 1
    while len(res)<10:
        res.append(0)
    return res

print(prime_factorization(14440))
print(prime_factorization(247808))