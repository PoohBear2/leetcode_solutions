import collections
class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        c = collections.defaultdict(list)
        for i, n in enumerate(nums):
            c[n].append(i)
        
        res = [0] * len(nums)
        for val in c:
            arr = c[val]
            t_sum = sum(arr)
            l_sum = 0

            for n, idx in enumerate(arr):

                res[idx] += n * idx - l_sum

                num_right = len(arr) - n - 1
                res[idx] += (t_sum - l_sum - idx) - num_right * idx

                l_sum += idx
        return res


        
