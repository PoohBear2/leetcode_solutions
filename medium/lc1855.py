class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        i, j = 0, 0

        best = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                best = max(best, j - i)
                j += 1
            else:
                i += 1
                j = max(i, j)
        return best

