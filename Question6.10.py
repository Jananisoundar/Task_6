def has_subarray_with_zero_sum(nums):
    # Initialize an empty set to store the cumulative sums
    cumulative_sum_set = set()
    # Initialize the cumulative sum
    cumulative_sum = 0

    for num in nums:
        # Add the current number to the cumulative sum
        cumulative_sum += num

        # If the cumulative sum is zero or already exists in the set, we found a subarray with zero sum
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True

        # Add the cumulative sum to the set
        cumulative_sum_set.add(cumulative_sum)

    # If no subarray with zero sum is found, return False
    return False


# Example usage:
nums = [4, 2, -3, 1, 6]
result = has_subarray_with_zero_sum(nums)

if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
