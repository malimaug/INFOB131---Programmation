def max_and_min(numbers: list) -> tuple:
    """Function tells the biggest and smallest integers of the list and the amount of times they appear

    Parameters
    ----------
    numbers : list of positive integers (list)

    Returns
    -------
    nbr_max : the biggest integer of the list
    max_amount : the amount of appearences of the biggest number in the list (list)
    nbr_min: the smallest integer of the list
    max_amount : the amount of appearences of the smallest number in the list (list)
    """

    if len(numbers) == 1:
        return 0, 0, numbers[0], 1

    else:
        nbr_max, max_amount, nbr_min, min_amount = max_and_min(numbers[1:])

        if numbers[0] > nbr_max:
            nbr_max = numbers[0]
            max_amount = 1

        elif numbers[0] < nbr_min:
            nbr_min = numbers[0]
            min_amount = 1

        elif numbers[0] == nbr_max:
            max_amount += 1

        elif numbers[0] == nbr_min:
            min_amount += 1

        return nbr_max, max_amount, nbr_min, min_amount


print(max_and_min([5, 7, 9, 3, 4, 3, 7, 82, 6, 87, 87, 3, 1]))