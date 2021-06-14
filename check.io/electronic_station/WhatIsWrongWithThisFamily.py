# https://py.checkio.org/en/mission/wrong-family/
# Electronic Station
# What Is Wrong With This Family?
from collections import deque


def is_family(tree: list[list[str]]) -> bool:
    # There are no strangers in the family tree.
    if len(set(son for father, son in tree)) < len(tree):
        return False
    # Can you be a father to your father?
    if any([True if [son, father] in tree else False for father, son in tree]):
        return False
    # if son in fathers or father in sons
    return all([True if father in ['Logan'] + [son for father, son in tree] or son in [father for father, son in tree] else False for father, son in tree])


if __name__ == "__main__":
    print(is_family([["Logan", "Mike"], ["Alexander", "Jack"], ["Jack", "Logan"]]))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
        ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
        ['Jack', 'Mike'],
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
    ]) == False, 'Two fathers'
    print("Looks like you know everything. It is time for 'Check'!")
