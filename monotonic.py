number = input()
nums = number.split()
nums = list (map(int, nums))
x = len (nums)

def is_monotonic(nums):
    y = 1
    problem = 0
    for y in range(1, x):
        if min(nums) == nums[0]:
            if nums[y] >= nums[y - 1]:
                continue
            else:
                problem += 1
        elif max(nums) == nums[0]:
            if nums[y] <= nums[y - 1]:
                continue
            else:
                problem += 1
        else:
            return False
    if problem == 0:
        return True
    else:
        return False

print (is_monotonic(nums))
