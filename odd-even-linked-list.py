# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd,even,o,e=None,None,None,None
        a=1

        while True:
            if head!=None:

#Odd part of the node
                if a%2!=0:
                    if a==1: #head node creation
                        odd=ListNode(head.val)
                        o=odd
                    else:
                        odd.next=ListNode(head.val)
                        odd=odd.next
                    head=head.next
                    a+=1

#Even part of the node
                else:
                    if a==2: #head node creation
                        even=ListNode(head.val)
                        e=even
                    else:
                        even.next=ListNode(head.val)
                        even=even.next
                    head=head.next
                    a+=1
            else:
                break

#combining the head of the even part with the tail of the odd
        if odd!=None:
            odd.next=e
        return o
"""Complexity
Time complexity:

O(n)

Space complexity:
O(((n*2))+((n/2)*2))"""           
