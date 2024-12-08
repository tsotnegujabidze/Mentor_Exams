# 7)  Find All Prime Numbers in a Given Range

# Write a function that takes two integers, start and end, and returns a list of all prime numbers in the range [start, end]. A prime number is a number greater than 1 that has no divisors other than 1 and itself.

def primes(start, end):
    prime_nums = []
    for i in range(start, end + 1): # access every numbers between two arguments
        if i > 1: # OFC Check if the number is greater than 1
            prime = True # Variable used to track whether the number is prime or not
            for number in range(2,int(i*0.5) + 1): # The "formule" of finding prime numbers which i studied
                if i % number == 0: # Checking if the number is not prime, stopping if it is not
                    prime = False
                    break
            if prime: # using variable we created to determine whether we append numbers or not
                prime_nums.append(i) 
    return prime_nums # finally return the list which contains prime numbers

print(primes(1, 1))