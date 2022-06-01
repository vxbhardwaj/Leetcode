class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di_ct={}
        for i,j in enumerate(nums):
            if target-j in di_ct:
                return [di_ct[target-j],i]
            if j not in di_ct:
                di_ct[j]=i