class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return Counter(ransomNote)<=Counter(magazine)
        if len(ransomNote)>len(magazine):
            return False
        for letter in ransomNote:
            if letter in magazine:
                magazine=magazine.replace(letter,"",1)
            else:
                return False
        return True

    
# Time complexity: O(m) where m is the length of ransomNote
# Space complexity: O(1) as no extra space needed