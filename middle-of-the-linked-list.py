# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#My answer
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        m=0
        while True:
            if node!=None:
                m+=1
                node=node.next
            else:
                break
        m=m//2
        res=head
        for i in range(m):
            res=res.next
        return res
            
#Most efficient answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid,node=head,head
        while node and node.next:
            mid=mid.next
            node=node.next.next
        return mid
