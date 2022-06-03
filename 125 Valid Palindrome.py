class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(x for x in s if x.isalnum()).upper()
        return s==s[::-1]
        
#Time Complexity: O(n) because it's traversing the string 3 times: once for filtering
#alphanumeric characters, also for reversing the string, then comparing reversed with non-
#reversed
#Space Complexity: O(n): we need additional O(n) space to store the filtered string and its 
#reverse