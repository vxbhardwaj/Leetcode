class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list=[0]*len(nums)
        for i in range(len(nums)):
            list[(i+k)%len(nums)]=nums[i]
        nums[:]=list
