def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")

    if is_palindrome(text):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")