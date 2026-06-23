# Question 2: To find a set of prime numbers between two given numbers.

def find_primes(lower, upper):
    primes = []
    for num in range(max(2, lower), upper + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes
start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))
print(f"Prime numbers between {start} and {end}: {find_primes(start, end)}")