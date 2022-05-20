class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list=[]
        for i in nums:
            if i in list:
                return True
            else:
                list.append(i)
        return False
        