#!/usr/bin/python3

def fib(num):
	"""return the number at index `num` in the fibonacci sequence"""
    if num <= 2:
        return 1
    return fib(num - 1) + fib(num - 2)

# method 2: use `for` loop
def fib2(num):
	a, b = 1, 1
	for _ in range(num - 1):
		a, b = b, a + b
	return a


print(fib(6))  # 8
print(fib2(6))  # same result, but faster






