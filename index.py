# 1. USING SLICE METHOD

# Use the slice operation [start:end:step], 
#  -1 reverses a string.

# word= input(("Enter a string:"))
# if(word==word[::-1]):
#     print("a palindrome")
# else:
#     print("no")


# 2. USING A LIST
from tracemalloc import start


word = input(("Enter a string:"))
word = word.casefold()
rev_word = reversed(word)

if list(rev_word) == list(word):
    print("a palindrome")
else:
    print("no")

#3 TAKE ALL CHARACTERS, PUT THEM IN AN ARRAY THEN REVERSE

# def isPalindrome(str):
#     start = 0
#     end = len(str) - 1
#     while start < end:
#         c1 = str[start:].lower()
#         c2 = str[end:].lower()

#         if validChar(c1) and validChar(c2):
#             if c1 != c2:
#                 return False
#             start = start + 1
#             end = end - 1
#         if not validChar(c1) and not validChar(c2):
#             start = start + 1
#             end = end - 1
#             return True

#         def validChar(c):
#             return c.isalpha()

# isPalindrome()
