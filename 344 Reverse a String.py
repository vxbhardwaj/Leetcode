class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list=[]
        left=0
        right=len(numbers)-1
        
        while(left<=right):
            if numbers[left]+numbers[right]==target:
                list.extend([left+1, right+1])
                return list
                
            if numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        
        
        