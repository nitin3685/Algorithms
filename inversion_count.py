def inversion_count(nums):
    inv_count = 0
    len_nums = len(nums)
    if len_nums == 1:
        return nums,inv_count

    #Divide
    mid = len_nums // 2
    left,left_inv_count = inversion_count(nums[:mid])
    right,right_inv_count = inversion_count(nums[mid:])

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
            #no of inversion equals for the current element in "right" array is
            #the number of elements left in "left" ,as they will all be greater
            #than current element of "right" , but have lesser index, which is
            #the definition of an inversion
            inv_count += len(left[left_index:])

    if left_index < (len(left)):
        sorted_nums.extend(left[left_index:])
    else:
        sorted_nums.extend(right[right_index:])

    return sorted_nums,(left_inv_count+right_inv_count+inv_count)

#print(inversion_count([1,3,5,2,4,6]))
#print(inversion_count([8,7,6,5,4,3,2,1]))
