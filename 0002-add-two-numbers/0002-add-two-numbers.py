class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            columnSum = v1 + v2 + carry
            carry = int(columnSum // 10)
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
        