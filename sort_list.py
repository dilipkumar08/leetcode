# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        node=head
        if node:
            while node!=None:
                li.append(node.val)
                node=node.next
            node=head
            li.sort()
            while node!=None:
                node.val=li[0]
                li.pop(0)
                node=node.next
        return head
            
