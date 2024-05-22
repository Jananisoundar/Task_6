def find_min_in_rotated_sorted_array(nums):
    if not nums:
        return None  # Handle empty list case

    left, right = 0, len(nums) - 1

    # If the list is not rotated (i.e., already sorted in ascending order)
    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than right, the min is in the right part
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    # After the loop, left == right and pointing to the minimum element
    return nums[left]



rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]
print("The minimum element is:", find_min_in_rotated_sorted_array(rotated_sorted_list))
