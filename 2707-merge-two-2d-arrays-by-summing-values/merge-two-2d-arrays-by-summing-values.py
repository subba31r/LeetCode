class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        lp1, lp2 = 0, 0
        res = []
        n1, n2 = len(nums1), len(nums2)
        while lp1 < n1 and lp2 < n2:
            if nums1[lp1][0] == nums2[lp2][0]:
                res.append([nums1[lp1][0],nums1[lp1][1] + nums2[lp2][1]])
                lp1 += 1
                lp2 += 1
            elif nums1[lp1][0] < nums2[lp2][0]:
                res.append([nums1[lp1][0],nums1[lp1][1]])
                lp1 += 1
            else:
                res.append([nums2[lp2][0],nums2[lp2][1]])
                lp2 += 1
        while lp1 < n1:
            res.append([nums1[lp1][0],nums1[lp1][1]])
            lp1 += 1
        while lp2 < n2:
            res.append([nums2[lp2][0],nums2[lp2][1]])
            lp2 += 1
        return res