from typing import List


def sort_words(words: List[str]) -> List[str]:
    result = words.copy()
    result.sort(key=len, reverse=True)
    return result


def sort_numbers(numbers: List[int]) -> List[int]:
    result = numbers.copy()
    result.sort(key=abs)
    return result


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
