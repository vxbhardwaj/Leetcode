# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev,prev.next,slow=slow,prev,slow.next
        if fast:
            slow=slow.next
        while prev and prev.val==slow.val:
            prev=prev.next
            slow=slow.next
        
        return not prev

#Time Complexity O(n), where n is the number of nodes in the linked list
#Space complexity O(1), no extra memory is being used