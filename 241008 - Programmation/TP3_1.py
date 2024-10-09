def calculateTax(sale_amount: float, state: str):
    """Calculate the amount of tax to pay in a state

    Parameters
    ----------
    sale_amount: amount of sale (float)
    state: two character id of state (str)

    Notes
    -----
    sale amount is in [$] and state should be in one of the three following options or it won't be supported:
    - "CA" -> California
    - "NY" -> New York
    - "TX" -> Texas

    """

    if state == "CA":
        tax_rate = 7.25

    elif state == "NY":
        tax_rate = 8.875

    elif state == "TX":
        tax_rate = 6.25

    else:
        return "State not supported"

    tax_amount = sale_amount * tax_rate / 100
    return tax_amount

print(calculateTax(100, "CA"))