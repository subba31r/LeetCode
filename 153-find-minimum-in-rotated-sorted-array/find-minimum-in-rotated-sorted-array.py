class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        minEle = float('inf')
        while l <=r:
            mid = (l+r)//2
            minEle = min(minEle,nums[mid])
            if nums[mid] > nums[r]:
                l= mid+1
            else:
                r=mid-1
        return minEle
            