def sprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
t=int(input("times of prime numbers :"))
for i in range(t):
        n=int(input("Enter the n upto you want the prime numbers count:"))
        c=0
        for i in range(2,n+1):
            if sprime(i):
                c=c+1
        print("prime numbers count is",c)
