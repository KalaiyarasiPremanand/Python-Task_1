# Roated sorted list
nums=[5,6,7,2,3]
low,high = 0,len(nums)-1
while low<high:
    mid=(low+high)//2
    if nums[mid]>nums[high]:            # If middle element is greater than last element
        low=mid+1                       # Minimum is in right half  
    else:
        high=mid                        # Otherwise minimum is in left half(including mid)
print(" Minimum element is:",nums[low]) # Minimum element