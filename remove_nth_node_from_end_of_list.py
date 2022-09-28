# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        position=length-n
        if position==0:
            head=head.next
            return head
        prev=head
        for _ in range(1,position):
            prev=prev.next
            
        prev.next=prev.next.next
        return head
