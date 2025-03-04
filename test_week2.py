import unittest
from week2 import most_frequent_item, most_frequent_count, find_repeat_number, unique_array, only_unique_items, exclude_product, are_all_items_unique, list_cycle, three_sum, is_anagram, count

def test_count():
    result = count(['apple', 'banana', 'apple'])
    expectedOutput = {'apple': 2, 'banana': 1}

    if result == expectedOutput:
        print("Count test passed")
    else:
        print("Count test failed")
test_count()

def test_most_frequent_item():
    result = most_frequent_item([1,1,1,3,3,5,6])
    expectedOutput = 1
    if result == expectedOutput:
        print("Most frequent item test passed")
    else:
        print("Most frequent item test failed")

test_most_frequent_item()

def test_most_frequent_count():
    list = [1,1,2,2,2,2,7,7]
    expectedOutput = 4

    result = most_frequent_count(list)

    if result == expectedOutput:
        print("Most frequent count test passed")
    else:
        print("Most frequent count test failed")
test_most_frequent_count()

def test_find_repeat_number():
    list = [2,3,4,5,3,6]
    expectedOutput = 3

    result = find_repeat_number(list)

    if result == expectedOutput:
        print("Find repeat number test passed")
    else:
        print("Find repeat number test failed")
test_find_repeat_number()

def test_unique_array():
    list = [1,2,2,3,4,3,5,]
    expectedOutput = [1,2,3,4,5]

    result = unique_array(list)

    if result == expectedOutput:
        print("Unique array test passed")
    else:
        print("Unique array test failed")
test_unique_array()

def test_only_unique_items():
    list = [2,3,3,4,5,5,6]
    expectedOutput = [2,4,6]

    result = only_unique_items(list)

    if result == expectedOutput:
        print("Only unique items test passed")
    else:
        print("Only unique items test failed")
test_only_unique_items()

def test_are_all_items_unique():
    nums = [1,2,3,4,5]
    expectedOutput = True
    result = are_all_items_unique(nums)

    if result == expectedOutput:
        print("Are all items unique test passed")
    else:
        print("Are all items unique test failed")
test_are_all_items_unique()

def test_list_cycle():
    list = [2,0,1]
    expectedOutput = True
    result = list_cycle(list)

    if result == expectedOutput:
        print("List cycle test passed")
    else:
        print("List cycle test failed")
test_list_cycle()

def test_three_sum():
    nums = [1,2,3,4,5]
    goal = 6
    result = three_sum(nums,goal)

    expectedOutput = [0,1,2]
    if result == expectedOutput:
        print("Three Sum test passed")
    else:
        print("Three Sum test failed")
test_three_sum()

def test_is_anagram():
    s1 = "A gentleman"
    s2 = "Elegant man"
    result = is_anagram(s1,s2)

    if result:
        print("Is anagram test passed")
    else:
        print("Is anagram test failed")
test_is_anagram()

def test_exclude_product():
    nums = [1,2,3,4]
    expectedOutput = [24, 12, 8, 6]
    result = exclude_product(nums)

    if result == expectedOutput:
        print("Exclude product test passed")
    else:
        print("Exclude product test failed")
test_exclude_product()
