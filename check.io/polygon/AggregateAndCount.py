# https://py.checkio.org/en/mission/aggregate-and-count/
from collections import defaultdict


def aggregate_and_count(items: list) -> dict:
    d = defaultdict(int)  # your code here
    for item in items:
        d[item[0]] += item[1]
    return d


print("Example:")
print(aggregate_and_count([["a", 1], ["b", 2], ["c", 3], ["a", 5]]))

assert aggregate_and_count([["a", 1], ["b", 2]]) == {"a": 1, "b": 2}
assert aggregate_and_count([["a", 1], ["a", 2]]) == {"a": 3}
assert aggregate_and_count([["a", 1], ["b", 2], ["c", 3], ["a", 5]]) == {
    "a": 6,
    "b": 2,
    "c": 3,
}
assert aggregate_and_count([["a", 1]]) == {"a": 1}

print("The aggregation is done! Click 'Check' to earn cool rewards!")
