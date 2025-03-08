#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime
from NumberTests import getFactors

def main():
  """ Return boalean (True/False) if the value given is prime."""""
  if p == 2:
    return True
  if isEven(p):
    return False
  
  for div in range(3, p // 2,2):
    if p % div == 0:
      return False
    
    return True

if __name__ == '__main__':
  main()