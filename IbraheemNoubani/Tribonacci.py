#!/usr/bin/python3
# Tribonacci.py prints the nth term of the tribonacci sequence

def tribonacci(n): 
    if (n < 1): 
        raise ValueError("N must be greater than 1") 

    first = second = 0
    third = 1 

    print(first, " ", end="") 
    if (n > 1): 
        print(second, " ", end="")
    if (n > 2): 
        print(second, " ", end="") 

    for i in range(3, n): 
        curr = first + second + third 
        first = second 
        second = third 
        third = curr

        print(curr, " ", end="") 

def main(): 
    n = int(input("Nth tribonacci number ")) 
    tribonacci(n)  

main() 
