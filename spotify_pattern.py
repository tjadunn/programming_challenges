from typing import List
from collections import defaultdict


def most_visited_pattern(
    username: List[str], timestamp: List[int], website: List[str]
) -> List[str]:
    """
    Accepts:
        username: (List[str]) The list of users who visited a website
        timestamp: (List[int]) The timestamp at which a user visited a website
        website: (List[str]) The website which the user visited

    Returns:
        pattern: (List[str]) The list of the most commonly visited website patterns
        i.e. the sequence of websites which received the most amount  visits in total

    Example:

        username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
        timestamp = [1,2,3,4,5,6,7,8,9,10],
        website = ["home","about","career","home","cart","maps","home","home","about","career"]

        Output: ["home","about","career"]

    Explanaintion:
        Joe and Mary both visited home, about and career twice. This is the highest number
        of sequential visits
    """
    # outline
    # get the triples of users who visited websites and at which time
    # e.g (joe, 1, home), (joe, 2, about) .... (mary, 10, career)
    # find all sequential sequences
    # find the patterns in these sequences
    # group by pattern -> count equivilant
    # find highest count and return pattern

    # This assumes that the lists are sorted in time order
    # for each  username
    # while the timestamp is increasing
    #  find every 3pattern
    #  add that pattern to a map
    #  continue over entire list of tuples until we've mapped every sequence
    #
    # if all visits are ordered by user we can use a deque -> sliding window

    triple = list(zip(username, timestamp, website))
    site_mapping = defaultdict(lambda: 0)


    return site_mapping


def test_most_visited_pattern() -> None:
    username = [
        "joe",
        "joe",
        "joe",
        "james",
        "james",
        "james",
        "james",
        "mary",
        "mary",
        "mary",
    ]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = [
        "home",
        "about",
        "career",
        "home",
        "cart",
        "maps",
        "home",
        "home",
        "about",
        "career",
    ]

    print(most_visited_pattern(username, timestamp, website))


#  assert most_visited_pattern(username, timestamp, website) == [
#      "home",
#      "about",
#      "career",
#  ]
#
if __name__ == "__main__":
    test_most_visited_pattern()
