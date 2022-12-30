from typing import List
"""
Leetcode linked list examples
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        if self.next == None:
            self.next = ListNode(val)
        else:
            self.next.insert(val)

    def print_list(self):
        print(self.val)
        if self.next:
            self.next.print_list()

    def __iter__(self):
        yield self.val
        next_node = self.next
        while next_node:
            yield next_node.val
            next_node = next_node.next


def create_list(input_values: List[int]) -> ListNode:
    """
    Helper function to create a linked list from a list of integers

    Accepts (List[int]): Sequence of values to input
    Returns (ListNode): The root list node of the linked list
    """

    root = ListNode(input_values[0])

    for value in input_values[1:]:
        root.insert(value)

    return root


def reverse_linked_list(node: ListNode) -> ListNode:
    """
    Given a linked list root->...->tail - reverse it

    Accepts (ListNode): The linked list to reverse
    Returns (ListNode): Tail node of the previous list which makes the new root

    Example:
        1->2->3->4

        returns

        4->3->2->1
    """

    current = node
    previous = None

    while current != None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def add_two_numbers(list_one: ListNode, list_two: ListNode) -> ListNode:
    """
    Given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a
    single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero,
    except the number 0 itself.

    Accepts (ListNode, ListNode): Two linked lists in question
    Returns: (ListNode): A new linked list of the summation of both ListNodes

    Example:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]

        Explanation: 342 + 465 = 807.
    """

    # Simple
        # outline
        # traverse each linked list
        # perform atoi equvilant
        # add together
        # form new linked list from digits
        #
    # More complex -> less space, maybe faster?
        # form a new linked list on the fly by summing the digits
        # and carrying the remaineder modulo 10 over from the previous element

    pointer_one = (list_one)
    pointer_two = (list_two)

    summation_list = ListNode()

    carry = None
    while pointer_one != None and pointer_two != None:
        new_val = (pointer_one.val + pointer_two.val) % 10

        if carry:
            new_val = new_val + carry
            carry = None

        if(pointer_one.val + pointer_two.val  >= 10):
            carry = 1

        summation_list.insert(new_val)

        pointer_one = pointer_one.next
        pointer_two = pointer_two.next

    return summation_list.next


def is_linked_lists_equal(list_one: ListNode, list_two: ListNode) -> bool:
    for val1, val2 in zip(list_one, list_two):
        if val1 != val2:
            return False

    return True

def test_add_two_numbers() -> None:

    list_one = create_list([2,4,3])
    list_two = create_list([5,6,4])
    list_three = create_list([7,0,8])

    list_one.print_list()
    print("")
    list_two.print_list()

    result = add_two_numbers(list_one, list_two)
    assert is_linked_lists_equal(result, list_three)


if __name__ == "__main__":
    test_add_two_numbers()

