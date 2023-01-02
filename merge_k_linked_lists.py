from typing import List
from queue import PriorityQueue

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        if not self.next:
            self.next = ListNode(val)
        else:
            self.next.insert(val)

    def delete(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def print_list(self):
        print(self.val)
        if self.next:
            self.next.print_list()

    def __iter__(self):
        yield self.val

        temp = self.next
        while temp:
            yield temp.val
            temp = temp.next


def merge_linked_lists(*nodes: ListNode) -> ListNode:
    """
    Given two sorted linked lists, return the merged sorted result

    Accepts:
        (ListNode) node_one : Sorted linked list one
        (ListNode) node_two : Sorted linked list two

    Returns:
        (ListNode) The sorted result of list_one merged with list_two

    Example:
        Input
            1->2->3->4->5
            5->6->7->8->9

        Output:
            1->2->3->4->5->6->7->8->9
    """

    # outline
    # maintain two pointers to the linked list heads and traverse them both
    # also maintain a priorirty queue to see which should be the next candidate node
    # in the result

    pq = PriorityQueue()

    for values in zip(*nodes):
        for value in values:
            pq.put(value)

    root = ListNode(pq.get(block=False))

    while not pq.empty():
        root.insert(pq.get(block=False))

    return root


def test_merge_linked_lists() -> None:
    list_one = ListNode(1)
    list_one.insert(2)
    list_one.insert(3)
    list_one.insert(4)
    list_one.insert(5)


    list_two = ListNode(5)
    list_two.insert(6)
    list_two.insert(7)
    list_two.insert(8)
    list_two.insert(9)

    result = merge_linked_lists(list_one, list_two)
    result.print_list()

if __name__== "__main__":
    test_merge_linked_lists()
