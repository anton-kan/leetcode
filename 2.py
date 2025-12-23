# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        current = result
        prev = None
        carry_over = 0
        while l1 != None or l2 != None:
            a = l1.val if l1 != None else 0
            b = l2.val if l2 != None else 0
            c = a + b + carry_over
            current.val = c % 10
            if prev != None:
                prev.next = current
            prev = current
            current = ListNode()
            carry_over = c // 10
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry_over > 0:
            current.val = carry_over % 10
            if prev != None:
                prev.next = current
        return result
        

def linkedListFromList(l):
    result = ListNode()
    current = result
    prev = None
    for i in l:
        current.val = i
        if prev != None:
            prev.next = current
        prev = current
        current = ListNode()
    return result

def printLinkedList(ll):
    result='['
    while ll != None:
        result += str(ll.val)
        result += ','
        ll = ll.next
    result = result.strip(',')
    result +=']'
    print(result)

l1 = linkedListFromList([9,9])
printLinkedList(l1)
l2 = linkedListFromList([9])
printLinkedList(l2)
printLinkedList(Solution().addTwoNumbers(l1, l2))