
def parity(n: int):
    """checks the parity of a number and displays the result

    Parameters
    ----------
    n: an integer (int)
    """
    if n % 2 == 0:
        print("n=%d even" % n)
    else:
        print("n=%d odd" % n)

for number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    parity(number)


