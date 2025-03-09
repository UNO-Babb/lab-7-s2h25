from NumberTests import isPrime

def generate_largest_pandigital():
    """Generate the largest p-digit pandigital number and check prime"""
    #Start from the largest 7-digit
    for num in range(7654321, 1234566, -2):
        if set(str(num)) == set("1234567") and isPrime(num):
            return num
        

    return None

def main():
    result = generate_largest_pandigital()
    print(f"Largest pandigital prime: {result}")
  

if __name__ == '__main__': 
    main()