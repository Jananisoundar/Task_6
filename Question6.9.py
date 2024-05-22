def find_triplet_with_sum(nums, target_sum):
    # Sort the list first
    nums.sort()
    n = len(nums)

    # Iterate through the list and use two pointers for the remaining two numbers
    for i in range(n - 2):
        # Initialize two pointers
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target_sum:
                return (nums[i], nums[left], nums[right])
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    # If no triplet is found
    return None



nums = [10, 20, 30, 9]
target_sum = 59
result = find_triplet_with_sum(nums, target_sum)

if result:
    print("Triplet found:", result)
else:
    print("No triplet found with the given sum.")
