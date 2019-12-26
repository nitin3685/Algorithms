def merge_sort(nums):

    len_nums = len(nums)
    if len_nums == 1:
        return nums

    #Divide
    mid = len_nums // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    #Merge
    sorted_nums = list()
    left_index,right_index = 0,0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_nums.append(left[left_index])
            left_index += 1
        else:
            sorted_nums.append(right[right_index])
            right_index += 1
    if left_index < (len(left)):
        sorted_nums.extend(left[left_index:])
    else:
        sorted_nums.extend(right[right_index:])

    return sorted_nums
