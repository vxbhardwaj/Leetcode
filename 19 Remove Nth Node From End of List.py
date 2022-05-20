# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find length of the list first
        length=0
        currentnode=head
        while (currentnode):
            length+=1
            currentnode=currentnode.next
        nodebeforenthfromright=head
        for i in range(length-n-1):
            nodebeforenthfromright=nodebeforenthfromright.next
        nodebeforenthfromright.next=nodebeforenthfromright.next.next
        
        return head
            