class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while(right>=left):
            pivot=(left+right)//2
            if target==nums[pivot]:
                return pivot
            elif target<nums[pivot]:
                right=pivot-1
            else:
                left=pivot+1
        return -1
                
#Time complexity: O(log n) using master's theorem
#Space complexity: O(1) since it's constant space solution