def isprime(n):
    for i in range (2,n):
        if n%i==0:
            return False
    return True

t=int(input("number of operations:"))
for i in range(t):
    n=input("Enter the range :").split()
    x=int(n[0])
    y=int(n[1])
    c=0
    for i in range(x+1,y):
        if isprime(i):
            c=c+1
    print("count is ",c)
