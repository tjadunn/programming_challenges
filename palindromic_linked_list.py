from typing import List

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None
    def insert(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.insert(val)

    def delete(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def delete_at_index(self, index):
        temp = self
        counter = 0
        while temp != None:
            previous = temp
            temp = temp.next

            counter += 1
            if counter == index:
                previous.next = temp.next

def reverse_linked_list(node: ListNode) -> ListNode:
    """
    Reverse a linked list

    Accepts ([ListNode]): The linked list to reverse
    Returns ([ListNode]): The head of the reversed linked list (previous tail)
    """

    current = node
    previous = None

    while node != None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def is_linked_list_palindrome(node: ListNode) -> bool:
    """
    Return the result of the predicate asking wether a linked list is a palindrome

    Accepts ([ListNode]) node: linked list to check
    Returns (bool) : The result of the predicate, yes if palinfrome, no if not
    """

    # Two solutions
    # easy solution -> reverse linked list and loop through the two. should be equal
    # o(1) space and o(n) complexity solution -> loop through once, get length,
    # loop through again and at the middle reverse the polarity of the digits,
    # total sum should equal 0 :)
    #
    pass
