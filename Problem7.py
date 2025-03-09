#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def nth_prime(p):
    """Return the nth prime number"""
    count = 0
    num = 1

    while count < p:
        num += 1
        if isPrime(num):
           count += 1
    
    return num

def main():
    p = 10001
    result = nth_prime(p)
    print(f"The {p}th prime number is: {result}")
  

if __name__ == '__main__': 
    main()