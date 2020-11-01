import time

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def fib(n):
    global count
    count += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

def fib_efficient(n, d):
    global count
    count += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1 : 1, 2 : 2}

argToUse = 34
print("")
print("Using fib")
count = 0
start = time.time()
print(fib(argToUse))
end = time.time()
print(end - start)
print("Count : " + str(count))
print("")
print("Using fib_efficient")
count = 0
start = time.time()
print(fib_efficient(argToUse, d))
end = time.time()
print(end - start)
print("Count : " + str(count))