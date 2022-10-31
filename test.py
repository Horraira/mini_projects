def removeElement(nums, val):
    size = len(nums)
    if size == 0 or (size == 1 and nums[0] != val):
        return size

    temp = list(range(size))
    j = 0
    for i in range(size):
        if nums[i] != val:
            temp[j] = nums[i]
            j = j + 1

    if j == 0:
        nums[:] = []

    for i in range(j):
        nums[i] = temp[i]

    return j


nums = [1,1,1]
print(removeElement(nums, 1))
print(nums)