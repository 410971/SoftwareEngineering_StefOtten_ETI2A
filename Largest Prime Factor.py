def prime_factor(n):
    i = 2
    factors = []
    while i + i <=n:
       if n%i:
          i+=i
       else:
          n//=i
          factors.append(i)

        if n >1:
            factors.append(n)
            return factors

number = 600851475143
print(prime_factor(number))
