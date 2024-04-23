def findPivotIndex(nums, left, right):
    pivot = nums[right]
 
   
    position = left 
 
    for index in range(left, right):
        if nums[index] < pivot:
            temp = nums[position]
            nums[position] = nums[index]
            nums[index] = temp 
            position += 1 
 
    temp = nums[right]
    nums[right] = nums[position]
    nums[position] = temp 
    return position
 
 
def performQuickSort(nums, left, right):
    if left >= right:
        return 
    pivotIndex = findPivotIndex(nums, left, right)
