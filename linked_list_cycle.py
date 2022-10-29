# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            if head==None or head.next.next==None:
                return False
            else:
                n1=head
                n2=head.next.next
                while n1.next!=None and n2.next.next!=None:
                    if n1==n2:
                        return True
                    n1=n1.next
                    n2=n2.next.next
        except:
            return False
