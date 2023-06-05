import re


def is_palindrome(line: str) -> bool:
    word = re.sub(r'\W', '', line.lower())
    return word == word[::-1]

print(is_palindrome(input().strip()))
