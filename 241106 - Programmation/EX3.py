killed = ['cow', 'cow', 'dog', 'cow']

def determine_points(victim_list: list) -> int:
    """
    The function returns the amount of points used by the hunter determined by its kills

    Parameters
    ----------
    victim_list : the list of killed things (list)

    Returns
    -------
    result: the amount of points used by the hunter (int)
    """
    points = 0
    victim_value = {'chicken': 10,
                    'dog': 30,
                    'cow': 50,
                    'human': 80}

    for victim in victim_list:
        points += victim_value[victim]

    return points

def determine_cost(victim_list: list) -> int:
    """
    The function returns the amount of money used by the hunter to perform the given hunt

    Parameters
    ----------
    victim_list : the list of killed things (list)

    Returns
    -------
    result: the amount of money used by the hunter (int)
    """

    points = determine_points(victim_list)
    money = 0

    modulo100 = points % 100
    amount_100points = points + (100 - modulo100)
    permit_amount = amount_100points / 100

    money += ((permit_amount - 1 ) * 200)

    if money < 0:
        money = 0

    return int(money)

killed = []

print("You will have to pay %d euros" % determine_cost(killed))
