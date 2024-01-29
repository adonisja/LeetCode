'''Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
added = ListNode(val = (l1.val + l2.val) % 10)
carry = (l1.val + l2.val) // 10
current_node = added
while(l1.next or l2.next):
    if l1.next:
        l1 = l1.next
    elif (not l1.next) and l2.next:
        l1.next = 0
    if l2.next:
        l2 = l2.next
    elif (not l2.next) and l1.next:
        l2.next = 0
    
    current_node.next = ListNode(val = (l1.val + l2.val + carry) % 10)
    carry = (carry + l1.val + l2.val) // 10
    current_node = current_node.next

    if carry > 0:
        current_node.next = ListNode(val = 1)
    
    return(added)