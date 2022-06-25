# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=1,n
        while(left<right):
            mid=left+(right-left)/2
            if (isBadVersion(mid)):
                right=mid
            else:
                left=mid+1
        return left

# Time Complexity: logn, binary search using master's theorem
# Space Complexity: O(1)