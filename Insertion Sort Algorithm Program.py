def insertionsort(nums):
    n=len(nums)
    
    for i in range(1,n):
        temp = nums[i]
        pos = i -1
        while pos>= 0 and nums[pos]>temp :
            nums[pos+1]=nums[pos]
            pos -=1
            nums[pos+1]=temp
        
        
        
n= int(input())
nums = list(map(int,input().split()))

insertionsort(nums)
for i in range(n):
    print(nums[i],end = " ")
