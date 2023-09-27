# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev=None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next  # return mid
            fast = fast.next.next
        cur=slow.next
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        slow.next = None
        p1, p2 = head, prev
        while p2:
            temp = p1.next
            p1.next = p2
            p1 = p2
            p2 = temp 