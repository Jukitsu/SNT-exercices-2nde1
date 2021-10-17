# Exercice 1

def pgcd(a, b):
    return pgcd(b, a%b) if b and a % b else b

def irreductible_frac(frac):
    p, q = frac
    a = pgcd(p, q)
    return (p // a, q // a)

def sum_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    n = pgcd(b, d)
    a2, b2, c2, d2 = a, b, c, d
    a2 *= (d // n)
    b2 *= (d // n)
    c2 *= (b // n)
    d2 *= (b // n)
    return irreductible_frac((a2 + c2, b2))

# Exercice 2

import math

def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if not n % i and n != i:
            return False
    return True

def prime_factors(n):
    primes = []
    primes_in = []
    
    for l in range(2, n + 1):
        if is_prime(l):
            primes_in.append(l)
    print(primes_in)
    while n != 1:
        for p in primes_in:
            if not n % p:
                n //= p
                primes.append(p)
                break
            else:
                primes_in.remove(p)
    primes.sort()
    return primes

if __name__ == "__main__":
    print(prime_factors(4410))

# Exercice 3

def divs(n):
    y = []
    for i in range(1, math.floor(math.sqrt(n))+1):
        if not n % i:
            y.append(n)
            y.append(n // i)
    return y

def is_perfect(n):
    divisors = divs(n)
    divisors.remove(n)
    return sum(divisors) == n

if __name__ == "__main__":
    for x in range(14):
        print(f"{x} est ", "parfait" if is_perfect(x) else " pas parfait")

        