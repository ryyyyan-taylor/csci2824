def binom_product(a,b,n) :
    import math
    product = 1
    for k in range(0, n + 1) :
        product *= (math.factorial(n) / (math.factorial(n - k) * math.factorial(k))) * pow(a, n - k) * pow(b, k)
    return product
