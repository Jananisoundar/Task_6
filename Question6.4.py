def sum_of_first_and_last_digit(n):
    # Convert the number to a string to easily access the first and last digits
    num_str = str(abs(n))  # Use abs to handle negative numbers
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    return first_digit + last_digit


# Example usage:
number = 12345
result = sum_of_first_and_last_digit(number)
print(f"The sum of the first and last digit of {number} is: {result}")
