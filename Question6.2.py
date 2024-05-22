def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_and_collect_primes(nums):
    """Return a tuple with the count of prime numbers and a list of prime numbers in nums."""
    prime_list = []
    for num in nums:
        if is_prime(num):
            prime_list.append(num)
    prime_count = len(prime_list)
    return prime_count, prime_list

nums = [10, 501, 22, 37, 100, 999, 87, 351]
prime_count, prime_list = count_and_collect_primes(nums)

print(f"Number of prime numbers: {prime_count}")
print(f"List of prime numbers: {prime_list}")
