
def parity(number: int):
    """The function returns True or False if the entered number is even or odd

    Parameters
    ----------
    number : the number to check (int)

    Returns
    -------
    parity : True if the number is even, False if odd (bool)

    Note
    ----
    If the input number isn't a whole number the function returns ("error: not a whole number")

    """
    if number % 2 == 0:
        return True
    elif number % 2 == 1:
        return False
    else:
        return "error: not a whole number"


nbr = 24

if parity(nbr):
    print("The number is even")
else:
    print("The number is odd")

