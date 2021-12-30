num = int(input())


def fibonacci(n):
	#complete the recursive function
    if n <= 1:
        return n
    
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)

for a in range(num):
    print((fibonacci(a)))

fibonacci(num)