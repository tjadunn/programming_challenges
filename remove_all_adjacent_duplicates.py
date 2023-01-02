from collections import Counter


def remove_duplicate_substrings_of_length_k(input_string: str, k: int) -> str:
    """
    You are given a string s and an integer k, a k duplicate removal consists of
    choosing k adjacent and equal letters from s and removing them,
    causing the left and the right side of the deleted substring to concatenate together.

    We repeatedly make k duplicate removals on s until we no longer can.

    Accepts (str) input_string: The string to deduplicate
            (int) k: the length of substring to find

    Returns
            (str) The string with all length k substrings removed

    Example:
        Input:
            s = "deeedbbcccbdaa", k = 3
        Output:
            "aa"
        Explanation:
            First delete "eee" and "ccc", get "ddbbbdaa"
            Then delete "bbb", get "dddaa"
            Finally delete "ddd", get "aa"
    """

    if input_string == "":
        return ""

    # outline
    # find all substrings of length k
    # Use a stack
    # iterate through the string
    # if the character was the same as the one before incremenet the count on the top
    # of the stack
    # if the count on the top of the stack equals k, erase the last k chars and pop 
    # from the stack
    #
    #
    occurance_stack = []
    index = 0

    while index < len(input_string):
        if index == 0 or input_string[index] != input_string[index-1]:
            occurance_stack.append(1)
        else:
            if input_string[index] == input_string[index-1]:
                occurance_stack[-1] += 1

        if occurance_stack[-1] == k:
            import ipdb; ipdb.set_trace()
            occurance_stack = occurance_stack[:-1]
            input_string = input_string[:index-k+1] + input_string[index + k:]

            # dont get ahead of ourselves as the string is now shorter
            index = index - (k+1)

        index += 1

    return input_string


def test_remove_duplicate_substrings_of_lenght_k() -> None:
    assert remove_duplicate_substrings_of_length_k("deeedbbcccbdaa", 3) == "aa"
    assert remove_duplicate_substrings_of_length_k("", 100) == ""


if __name__ == "__main__":
    test_remove_duplicate_substrings_of_lenght_k()
