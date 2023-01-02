from collections import deque
from typing import List
import ipdb

"""

Leetcode strings and array problems
Dec 2022

"""

def permute(string_s) -> List[str]:
    out = []
    if len(string_s) == 1:
        return [string_s]
    else:
        for index, letter in enumerate(string_s):
            for perm in permute(string_s[0:index] + string_s[index + 1 :]):
                out += [letter + perm]

    return out


def longest_substring(input_string: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

        Accepts (str): input_string in question
        Returns (str): length of longest substring

    Runs in O(2n)
    """

    if input_string == "":
        return 0

    len_max = 1

    for index, letter in enumerate(input_string):
        substring_idx = index + 1
        max_counter = 1

        candidates = set()
        candidates.add(letter)

        while (
            substring_idx < len(input_string) - 1
            and input_string[substring_idx] not in candidates
        ):
            candidates.add(input_string[substring_idx])
            max_counter += 1
            substring_idx += 1

        if max_counter > len_max:
            len_max = max_counter

    return len_max


def find_longest_palindromic_substring(input_string: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s

        Accepts(str): input_string in question
        Returns(str): the longest palindromic substring of input_string

    Example:

        Input: "babad"
        Output: "bab"

        Explanation: "aba" is also a valid answer.
    """

    max_string = ""
    max_counter = 1

    for index, letter in enumerate(input_string):
        substring_idx = index + 1

        while substring_idx < len(input_string):
            if (
                is_palindrome(input_string[index:substring_idx])
                and len(input_string[index:substring_idx]) > max_counter
            ):
                max_string = input_string[index:substring_idx]
                max_counter = len(max_string)

            substring_idx += 1

    return max_string


def is_palindrome(input_string: str) -> bool:
    end = len(input_string) - 1

    if input_string == "":
        return False

    for start in range(0, int(len(input_string) / 2)):
        if input_string[start] != input_string[end]:
            return False
        end -= 1

    return True


def has_increasing_subsequence(input_list: List[int]) -> bool:
    """

    Given an integer array nums, return true if there exists a
    triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
    If no such indices exists, return false.

        Accepts (List[int]): input_list of integers to check
        Returns (bool): Whether the predicate is satisfied

    Example:
        [1, 2, 3, 4, 5]
        returns True

        [5, 4, 3, 2, 1]
        returns False

    """

    if len(input_list) < 3:
        return False

    # window bound
    upper_index = 2

    triplet_window = deque()
    triplet_window.extend(input_list[0:upper_index+1])

    while True:
        if is_increasing(
            triplet_window[0],
            triplet_window[1],
            triplet_window[2],
        ):
            return True

        upper_index += 1

        if upper_index >= len(input_list):
            return False

        triplet_window.popleft()
        triplet_window.append(input_list[upper_index])



def is_increasing(i: int, j: int, k: int) -> bool:
    """
    Helper function abstracted for tests
    """
    return i < j < k


def test_has_increasing_subsequence() -> None:
    assert has_increasing_subsequence([1, 2, 3, 4, 5]) == True
    assert has_increasing_subsequence([5, 4, 3, 2, 1]) == False
    assert has_increasing_subsequence([2, 1, 5, 0, 4, 6]) == True


def test_is_palindrome() -> None:
    assert is_palindrome("aaaa") == True
    assert is_palindrome("aaa") == True
    assert is_palindrome("bab") == True
    assert is_palindrome("") == False
    assert is_palindrome("abcd") == False
    assert is_palindrome("aabaa") == True


def test_longest_palindrome() -> None:
    assert find_longest_palindromic_substring("babad") == ("bab" or "aba")
    assert find_longest_palindromic_substring("aaaa") == "aaa"
    assert find_longest_palindromic_substring("cbbd") == "bb"


def test_longest_substring() -> None:
    assert longest_substring("abcabcbb") == 3
    assert longest_substring("") == 0
    assert longest_substring("bbbbb") == 1
    assert longest_substring("pwwkew") == 3


def test_permute() -> None:
    assert permute("abc") == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

if __name__ == "__main__":
    test_permute()
    test_longest_substring()
    test_is_palindrome()
    test_longest_palindrome()
    test_has_increasing_subsequence()
