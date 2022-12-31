from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, val):
        if self.next == None:
            self.next = ListNode(val)
        else:
            self.next.insert(val)

    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.nex

    def delete(self, index):
        temp = self
        counter = 0
        while temp is not None:
            prev = temp
            temp = temp.next
            counter += 1

            if counter == index:
                prev.next = temp.next
                break

    def print_list(self):
        print(self.val)
        if self.next:
            self.next.print_list()

def create_linked_list(input_list: List[int]) -> ListNode:
    """
    Helper method to construct a linked list

    Accepts (List[int]): The list of integers to construct the LL from
    Returns (ListNode): The head of the newly formed linked list

    Example:
        [1,2,3]

    Returns the head node of:
        1->2->3
    """
    root = ListNode(input_list[0])
    for node in input_list[1:]:
        root.insert(node)

    return node

def group_linked_list_odd_even(linked_list: ListNode) -> ListNode:
    """
    Given the head of a singly linked list, group all the nodes with odd indices
    together followed by the nodes with even indices, and return the reordered list

    The relative order inside both the even and odd groups is preserved

    Accepts (ListNode): The head of the list to group
    Returns (ListNode): The head of the grouped list

    Example:
        Input:  [1,2,3,4,5]
        Output: [1,3,5,2,4]
    """
    # outline
    # cycle through the list
    # if we encounter an odd indicie then continue
    # if we encounter an even indicie then swap it with the next even indicie
    #
    # if we know the length of the list then we can just re order the list
    # while we have even indicies left:
    # While node not None:
    # if the indidicie is even then delete and insert at the end of the list

    node = head = linked_list
    print("before")
    head.print_list()
    index = 0
    while node != None:
        # if we have an even index
        node.delete(index)
        node = node.next

    print("after")
    return node 

def test_delete_linked_list() -> None:
    root = ListNode(0)
    root.insert(5)
    root.insert(6)
    root.insert(7)

    root.delete(1)
    root.delete(2)

    root.print_list()

    print(" ")
    root = ListNode(0)
    root.insert(5)
    root.insert(6)
    root.insert(7)

    root.delete(3)
    root.delete(4)
    root.print_list()



def test_group_linked_list_odd_even() -> None:
    root = ListNode(0)
    root.insert(5)
    root.insert(6)
    root.insert(7)
    root.insert(8)

    result = group_linked_list_odd_even(root) 
    result.print_list()


if __name__ == "__main__":
    test_delete_linked_list()
    #test_group_linked_list_odd_even()
