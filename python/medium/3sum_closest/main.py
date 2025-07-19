def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()  # Sort the array to use two-pointer technique
    n = len(nums)
    closest_sum = float('inf')  # Initialize closest sum

    for i in range(n - 2):  # Iterate up to n-2 to leave room for two pointers
        left = i + 1
        right = n - 1
        while left < right:  # Use two pointers
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:  # If exact match, return immediately
                return current_sum
            # Update closest_sum if current_sum is closer to target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            # Adjust pointers based on whether current_sum is too large or too small
            if current_sum < target:
                left += 1
            else:  # current_sum > target
                right -= 1

    return closest_sum
