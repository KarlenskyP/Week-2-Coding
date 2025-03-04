# Warmups
import string
def count(items):
    """
    Given a list of items, return a dictionary with the count of each item.
    E.g. count(['a', 'b', 'a']) -> {'a': 2, 'b': 1}
    The items can be of any type.
    """
    count = {}
    for item in items:
            count[item] = count.get(item, 0) + 1
    return count

def most_frequent_item(nums):
    """
    Given a list of integers, return the most frequently occurring integer.
    If there are multiple answers, return the smallest one.
    If the list is empty, return -1
    """
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    if frequency:
        return min(frequency, key=lambda x: (-frequency[x], x))
    return -1

def most_frequent_count(nums):
    """
    Given a list of integers, count how many times each appears and then return the most frequent count.
    E.g. in [1, 1, 2, 2, 2, 7, 7, 7], both 2 and 7 appear 3 times, so return 3.
    There will only be one most frequent count.
    If the list is empty, return 0
    """
    if not nums:
        return -1
    frequency = {}

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return max(frequency.values())


def find_repeat_number(nums):
    """
    Given a list of integers, return the first number that appears twice. If there are no duplicates, return -1.
    """
    visited = set()

    for num in nums:
        if num in visited:
            return num
        visited.add(num)

    return -1


def unique_array(nums):
    """
    Given a list of integers, return a new list with the duplicates removed.
    The order of the elements should be the same as the original list.
    """
    unique_nums = []
    visited = set()

    for num in nums:
        if num not in visited:
            unique_nums.append(num)
            visited.add(num)
    
    return unique_nums

def only_unique_items(nums):
    """
    Given a list of integers, return a new list with only items that never appear more than once.
    Think about how this is different from the above problem.
    """
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    return [num for num in nums if count[num] == 1]

def are_all_items_unique(nums):
    """
    Given a list of integers, return True if all the items are unique, otherwise return False.
    """
    if len(nums) == len(set(nums)):
        return True
    else:
        return False

# Now that you're warmed up

def list_cycle(nums):
    """
    For this problem, you are given a list of integers. The integers in the list represent indices in the list.
    Starting at index 0, the value at index 0 points to the index of the next element.
    E.g. for the list [2, 0, 1] - starting at index 0 you go to index 2, from index 2 you go to index 1, and from index 1 you go to index 0.
    Return True if by starting at index 0 and following this pattern you can visit every index in the list, otherwise return False.
    If the list is empty, return True
    """
    if not nums:
        return True
    
    visited = set()
    current = 0

    while current not in visited:
        visited.add(current)
        current = nums[current]

        if current < 0 or current >= len(nums):
            return False
        
    return len(visited) == len(nums)

def three_sum(nums, goal):
    """
    Given a list of integers and a goal integer, return the indexes of three integers in the list sum to the goal integer.
    There will be either 0 or 1 answers. If there is no answer, return [-1, -1, -1].
    """
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            for c in range(b + 1, len(nums)):
                if nums[a] + nums[b] + nums[c] == goal:
                    return [a,b,c]
    return [-1, -1, -1]

def is_anagram(s1, s2):
    """
    Given two sentences, return True if they are anagrams of each other. Ignore case, spaces, and punctuation.
    Yes - this is the same as the week1 problem, but now I expect you to use a dictionary.
    """
    s1 = ''.join(e for e in s1 if e.isalnum()).lower()
    s2 = ''.join(e for e in s2 if e.isalnum()).lower()
    char_count1 = {}
    char_count2 = {}

    for char in s1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in s2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    if char_count1 == char_count2:
        return True
    else:
        return False


def exclude_product(nums):
    """
    Given a list of integers, return a new list where each element is the product of all the numbers in the input list except the number at that index.
    Do this in an O(n) solution, you do not need to use a nested loop.
    """
    n = len(nums)
    result = [1] * n

    product = 1
    for a in range(n):
        result[a] = product
        product *= nums[a]
    
    product =1
    for a in range(n - 1, -1, -1):
        result[a] *= product
        product *= nums[a]

    return result
