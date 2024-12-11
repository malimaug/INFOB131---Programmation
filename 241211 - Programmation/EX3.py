def is_palindrome(text: str):
    text = text.lower()
    text = text.replace(" ", "")

    if text == "":
        return True

    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])


print(is_palindrome("hello"))