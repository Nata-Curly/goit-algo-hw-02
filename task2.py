from collections import deque


def is_palindrome(string):
    '''checks if the string palindrome is'''
    # string = string.lower().replace(" ", "")
    string = "".join(char.lower() for char in string if char.isalnum())
    d = deque(string)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("Hello World!"))
print(is_palindrome("Karamba Abmarak"))
