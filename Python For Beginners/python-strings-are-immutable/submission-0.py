def remove_fourth_character(word: str) -> str:
    first=word[:3]
    second=word[4:]
    full=first+second
    return full


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
