def factorial(n):
    """Returns the factorial n!

    Parameters
    ----------
    n : strictly positive integer (int)

    Returns
    -------
    f : factorial of n (int)
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def word_lenght(word: str) -> int:
    if word == "":
        return 0
    else:
        return 1 + word_lenght(word[:-1])

print(word_lenght("hello"))