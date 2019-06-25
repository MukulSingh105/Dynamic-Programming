# RECURSIVE SOLUTION OF FIBONACCI SEQUENCE

def fib(n):
    if(n==1) or (n==0):
        result = 1
    elif (n>1):
        result = fib(n-1) + fib(n-2)
    else:
        raise Exception ("Negative Number Error") 
    return result
print(fib(5))




# DYNAMIC PROGRAMMING SOLUTIONS
# METHOD 1: TABULATION

def fibtab(n):
    fibtab = [0 for i in range(n+1)]
    fibtab[0] = fibtab[1] = 1
    if(n>1):
        for i in range(2,n+1):
            fibtab[i] = fibtab[i-1]+fibtab[i-2]
        result = fibtab[n]
    else:
        raise Exception ("Not a valid number")
    return result
print(fibtab(5))


# METHOD 2: MEMOIZATION

mem = [0 for i in range(1000)]
mem[0] = mem[1] = 1
def fibmem(n):
    if(mem[n]!=0):
        return mem[n]
    else:
        mem[n] = fibmem(n-1) + fibmem(n-2)
        return mem[n]
print(fibmem(5))

