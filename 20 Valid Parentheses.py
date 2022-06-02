class Solution:
    def isValid(self, s: str) -> bool:
        di_ct= {")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in di_ct and len(stack)!=0:
                if stack.pop()!=di_ct[i]:
                    return False
            else:
                stack.append(i)
        return len(stack)==0
            
            

# Time complexity: O(n) as going through the elements of the string once.
#push and pop take O(1). 
# Space complexity: O(n): in worst case we push all elements of the string to the stack.

