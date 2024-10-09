def currency_conversion(amount: float, currency: str):
    """Function which turns the indicated amount of euros or dollars into the opposite currency and returns it.

    Parameters
    ----------
    amount : amount to convert (float)
    currency : currency of amount (str)

    Returns
    -------
    result : converted currency (float)

    Notes
    -----
    Use "E" for euros and "S" for dollars.
    1 euro = 1.12586 dollars

    """
    if currency == "E":
        return amount * 1.12586
    elif currency == "S":
        return amount / 1.12586
    else:
        return "Incorrect currency"


# Je rajouterai une variable exchange_rate dans la fonction et dans la spécification. Dans la seconde je spécifierait que ce taux de change doit être la valeur du dollars pour 1 euro
# Version 2


def currency_conversion2(amount: float, currency: str, exchange_rate: float):
    """Function which turns the indicated amount of euros or dollars into the opposite currency and returns it.

    Parameters
    ----------
    amount : amount to convert (float)
    currency : currency of amount (str)
    exchange_rate : exchange rate (float)

    Returns
    -------
    result : converted currency (float)

    Notes
    -----
    Use "E" for euros and "S" for dollars.
    The exchange rate is the amount of dollars per euro.

    """
    if currency == "E":
        return amount * exchange_rate
    elif currency == "S":
        return amount / exchange_rate
    else:
        return "Incorrect currency"