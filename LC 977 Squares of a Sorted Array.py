class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list=[]
        left=0
        right=(len(nums)-1)
        for i in range(len(nums)):
            if abs(nums[left])<abs(nums[right]):
                list.append(nums[right]**2)
                right-=1
            else:
                list.append(nums[left]**2)
                left+=1
        return list[::-1]
            