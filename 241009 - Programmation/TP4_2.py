def stamp_amount(normalized: bool, weight: float):
    """The function returns de amount of stamps to put on a letter depending on the weight and type of envelope

    Parameters
    ----------
    normalized : tells if the envelope is normalized or not (bool)
    weight : the weight of the envelope (float)

    Returns
    -------
    return : returns the amount of stamps required for the envolope to send properly

    Notes
    -----
    Normalized should be True if it is or False if it isn't
    weight should be indicated in [g]

    """

    if not normalized:

        if weight <= 100:
            return 2
        elif weight <= 350:
            return 3
        elif weight <= 1000:
            return 5
        elif weight <= 2000:
            return 7
        else:
            return "weight exceeded allowed amount"

    elif normalized:
        return 1

    else:
        return "error: has to be either normalized or not"

    
