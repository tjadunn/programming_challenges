from typing import List

def is_valid_parenthisis(input_string: str) -> bool:
    """
    Accepts (str) input_string: An input string checking of parenthesis
    Returns (bool): Wether the predicate was satisfied or not

    Example:
        Input:
            "[][][][]"
        Returns:
            True

        Input:
            "[}{[}]"
        Returns:
            False
    """

    stack = []
    opening_brace = {"(", "{", "["}
    closing_brace = {")", "}", "]"}

    close_mapping = {"(": ")", "{": "}", "[": "]"}

    for paren in input_string:
        if paren in opening_brace:
            stack.append(paren)
        elif paren in closing_brace:
            if not stack:
                # started with a closing brace - must be False
                return False
            stack_peep = stack[-1]
            if close_mapping[stack_peep] == paren:
                stack = stack[:-1]

    #  have an empty stack to return True
    return not stack


def apply_operand(a: int, b: int, operand: str) -> int:
    if operand == "*":
        return a * b
    elif operand == "+":
        return a + b
    elif operand == "-":
        return a - b


def is_operand(a: str) -> bool:
    return a in {"+", "-", "*"}


def calculate_polish_notation(expression: str) -> int:
    """
    Given a Polish notation string, compute its result

    Accepts (str) expression: arithmetic expression to calculate
    Returns (int) result: the result of the calculation

    Example:

    input
        1 2 - 4 5 + *

        i.e

       (1 - 2) * (4 + 5)

    returns
        -9
    """
    stack = []

    for item in expression:
        if item.isdigit():
            stack.append(int(item))
        elif is_operand(item):
            new_value = apply_operand(stack[-2], stack[-1], item)
            stack = stack[:-2]
            stack.append(new_value)

    return stack[0]


def reverse_with_stack(string_s: str) -> str:
    """
    Reverse the given string using a stack

    stupid example just to prove a point :)
    """

    stack = []

    for letter in string_s:
        stack.append(letter)

    result = ""
    end = len(string_s)

    for index in range(1, end + 1):
        result += stack[-index]

    return result


def find_stock_span(stock_price: List[int], n: int) -> List[int]:
    """
    Given a series of n daily price quotes, calculate the span

    The span is defined as the number of consecutive days before the given day for which
    the stock price was less than the price on the given day

    Accepts (List[int]) stock_price: The stock prices
            (int)       n: the number of stock prices

    Returns (List[int]) The span for the given number of stock prices

    Example:
        Input:
            N = 7, price[] = [100 80 60 70 60 75 85]
        Output:
            [1 1 1 2 1 4 6]
    """
    # outline
    # brute force is to continue moving along the stock prices, while the previous
    # element is less than the current, increase the span by one. The span starts at 1
    # this will need to use a double loop O(n^2)
    #
    # smarter way could use an auxilary stack to keep track of things
    #
    # push 1 onto the stack,
    # while stack is non empty
    # if current element  is less than day element in question incremenet head of stack by one
    # once we reach an element that is greater than the element in question, pop the stack and return the value x
    # set the incremental index back - x places
    # repeat until we have an empty stack
    #
    #
    # This is a bit buggy and might infinite loop lul
    #
    stack = []
    result = []

    head = 0
    stock_price_index = head + 1

    # cheeky - easier to reason about in reverse
    stock_price.reverse()

    stack.append(1)
    while stock_price_index < n:

        if stock_price[stock_price_index] < stock_price[head]:
            # While we the stock price is still lower than our element in question

            # Keep count of how many days stocks its higher than
            stack[-1] += 1

            # Move onto the previous day
            stock_price_index += 1

        elif stock_price[stock_price_index] > stock_price[head]:
            result.append(stack[-1])
            stack = stack[:-1]

            head += 1
            stock_price_index = head + 1

            # prime the stack for the next candidate
            stack.append(1)



def test_find_stock_play() -> None:
    assert find_stock_span([100, 80, 60, 70, 60, 75, 85], 7) == [1, 1, 1, 2, 1, 4, 6].reverse()


def test_calculate_polish_notation() -> None:
    assert calculate_polish_notation("12-45+*") == -9


def test_is_valid_parenthisis():
    assert is_valid_parenthisis("[][][]") == True
    assert is_valid_parenthisis("") == True
    assert is_valid_parenthisis("{[()]}") == True
    assert is_valid_parenthisis("][") == False


if __name__ == "__main__":
    test_is_valid_parenthisis()
    test_calculate_polish_notation()
    test_find_stock_play()
