def is_happy_number(n):
    """Return True if n is a happy number, else False."""

    def get_next_number(num):
        return sum(int(char) ** 2 for char in str(num))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next_number(n)

    return n == 1


def count_happy_numbers(nums):
    """Return the count of happy numbers in the list nums."""
    happy_count = 0
    for num in nums:
        if is_happy_number(num):
            happy_count += 1
    return happy_count



nums = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = count_happy_numbers(nums)

print(f"Number of happy numbers: {happy_count}")

