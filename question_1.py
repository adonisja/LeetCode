''' Question 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. '''

nums = [2,7,11,15]
target = 13

''' First Attempt: #Uses double loops to loop t
for i in range(len(nums) - 1):
    for j in range(1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])'''

'''Second Attempt: uses enumerate and a dictionary'''
seen = {}           #creates a dictionary to store values that have been used
for i, num in enumerate(nums): #enumerates over the values in list of nums, taking note of the indices as well
    if target - num in seen:    #checks if the difference of target and nums (which is the key) is in the dictionary
        print(seen[target - num], i) 
        #prints the index (which is the value) of that difference as stored in seen and the index of the current number if that difference is present 
    elif num not in seen:
        seen[num] = i   #if num is not in seen then that num and its index is stored in seen (key=num, val=index) 


'''Third Attempt'''

