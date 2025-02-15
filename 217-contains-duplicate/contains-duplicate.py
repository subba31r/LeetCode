class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force method - O(n^2)
        #checking each element with every other element
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #Optimizing by sorting, for sorting it takes O(nlogn)
        # and for loop takes O(n) overall it is o(nlogn)
        # nums.sort()
        # for i in range(0,len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        #Time complexity is O(n) as accessing keys from dic takes only O(1)
        #and for loop takes O(n). So, overall is O(n)
        #Space complexity is O(n) as we are storing every element in dic
        dic = {}
        for i in range(0,len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]] = nums[i]
            else:
                return True
        return False

        #by using set instead of dictionary
        #O(n) time and space complexity
        # if len(nums) == len(set(nums)):
        #     return False
        # return True