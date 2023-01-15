from typing import List
from collections import defaultdict
from itertools import combinations


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
         Input:

            username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
            timestamp = [1,2,3,4,5,6,7,8,9,10],
            website = ["home","about","career","home","cart","maps","home","home","about","career"]

        Output:
            ["home","about","career"]

    Explanaintion:
        Joe and Mary both visited home, about and career twice. This is the highest number
        of sequential visits

    Raises:
        N/A
    """
    # outline
    # get the triples of users who visited websites and at which time
    # e.g (joe, 1, home), (joe, 2, about) .... (mary, 10, career)
    # find all sequential sequences
    # find the patterns in these sequences
    # group by pattern -> count equivilant
    # find highest count and return pattern

    # for each  username
    # while the timestamp is increasing
    #  find every 3pattern
    #  add that pattern to a hashmap
    #  continue over entire list of tuples until we've mapped every sequence
    #
    # if all visits are ordered by user we can use a deque -> sliding window


    # sort via username and timestamp - this will group users together so we can get sequences
    triple = sorted(zip(username, timestamp, website), key=lambda x: (x[0],x[1]))

    # create a mapping for each user with an ordered list of its site visits
    site_mapping = defaultdict(lambda: [])

    # basically for each username add its visisted site to a list of sites it visited
    # then translate this list and find all sequential combinations of it

    for username, timestamp, website in triple:
        site_mapping[username].append(website)

    pattern_visits = defaultdict(lambda: 0)

    for username, visits in site_mapping.items():
        for combination in combinations(visits, 3):
            pattern_visits[combination] +=1

    return max(pattern_visits.items(), key=lambda x: x[1])


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
