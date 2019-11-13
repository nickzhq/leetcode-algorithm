# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        meet_node = None
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                meet_node = slow
                break
        
        
        if meet_node != None:
            slow = head
            meet = meet_node
            while slow is not meet:
                slow = slow.next
                meet = meet.next
            return meet
        
        return None