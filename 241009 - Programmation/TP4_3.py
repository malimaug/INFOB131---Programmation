
def parity(number: float):
    """The function returns True or False if the entered number is even or odd

    Parameters
    ----------
    number : the number to check (float)

    Returns
    -------
    parity : True if the number is even, False if odd (bool)

    """
    if number % 2 == 0:
        return True
    else:
        return False


nbr = 24

if parity(nbr):
    print("The number is even")
else:
    print("The number is odd")

