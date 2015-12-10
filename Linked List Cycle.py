__author__ = 'Nick'

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slowPointer = fastPointer = head

        while fastPointer and fastPointer.next:

            slowPointer, fastPointer = slowPointer.next, fastPointer.next.next

            if slowPointer == fastPointer:
                return True

        return False
