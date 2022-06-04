class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_subarray=max_subarray=nums[0]
        for num in nums[1:]:
            cur_subarray=max(num,num+cur_subarray)
            max_subarray=max(max_subarray, cur_subarray)
        return max_subarray
        
    #Time complexity: O(n)- iterate through all elements once
    #Space complexity O(1) - regardless of the size of the list, only two variables used