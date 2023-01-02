from typing import List, Optional
import heapq

def find_kth_largest(nums: List[int], k: int) -> Optional[int]:
    """
    Given a list of integers, return the kth largest in the list

    Accepts nums (List[int]) k (int): The list of integers to search  
    Returns (int): The kth largest element

    Example:

    Inputs:
        nums = [3,2,1,5,6,4], k = 2

    Returns:
        4
    """
    # outline
    # for each element in the list
    # maintain a max heap and push each element onto the max heap
    # once we've reached the end of the list - pop the heap k times

    if nums == []:
        return None

    max_heap = []
    for item in nums:
        # heapq implements a min heap by default so multiply by -1
        heapq.heappush(max_heap, -item)

    for index in range(0, k-1):
       heapq.heappop(max_heap)

    kth_smalltest =  heapq.heappop(max_heap)
    return kth_smalltest

def test_kth_largest() -> None:
    assert find_kth_largest([3,2,1,5,6,4], 2) == -5
    assert find_kth_largest([], 0) == None
    assert find_kth_largest([3, 3, 3, 3,], 2) == -3


if __name__ == "__main__":
    test_kth_largest()
