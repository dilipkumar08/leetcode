# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentnode=head
        l=0
        while currentnode.next!=None:
            currentnode=currentnode.next
            l+=1
        if l==0:
            currentnode=head
            currentnode.val=''
            currentnode.next=None
        else:
            if l%2==0:
                l=int(l/2)
            else:
                l=(l//2)+1
            currentnode=head
            i=0
            while i<=l:
                if i==l :
                    if currentnode.next==None:
                        currentnode=head
                        currentnode.next=None
                    else:
                        currentnode.val=currentnode.next.val
                        currentnode.next=currentnode.next.next
                currentnode=currentnode.next
                i+=1
        return head
            
            
            
            
            
        
