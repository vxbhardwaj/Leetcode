#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i,j in enumerate(nums):
            if target-j in hashMap.keys():
                return [hashMap[target-j],i]
            else:
                hashMap[j]=i