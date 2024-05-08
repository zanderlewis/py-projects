# Difficulty: II

def is_palindrome(s):
    s = s.replace(' ', '').lower()
    return s == s[::-1]

s = input("Enter a word or sentence: ")
if is_palindrome(s):
    print(f"'{s}' is a palindrome!")
else:
    print(f"'{s}' is not a palindrome.")