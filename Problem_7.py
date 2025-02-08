#String Palindrome: Write a Python function to check if a given string is a palindrome or not.

word = input("Enter a 3-lettered word:")
if word[0] == word[-1] and word[1] == word[-2]:
    print("This word is a palindrome!"),
else:
    print("This word is not a palindrome!")

