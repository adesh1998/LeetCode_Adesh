# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ptr=head
        # len=0
        # while ptr:
        #     len+=1
        #     ptr=ptr.next
        # if len == n : return head.next
        # ptr = head
        # for i in range(1, len - n):
        #     ptr = ptr.next
        # ptr.next = ptr.next.next
        # return head
        fast,slow=head,head
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head



