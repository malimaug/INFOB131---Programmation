def get_ticket_price(base_price: float, days_before: int):
    """Returns the price of a flight depending on when the ticket was bought and the base price

    Parameters
    ----------
    base_price: the default price of the flight (float)
    days_before: amount of days between the moment the ticket was bought and the plane takes off (int)

    Returns
    -------
    final_price: the price after calculation of reduction or extra costs (float)

    """
    if days_before > 100:
        return base_price * 0.5
    elif days_before < 3:
        return base_price + 15 * (30 - days_before) + 100
    elif days_before < 30:
        return base_price + 15 * (30 - days_before)
    else:
        return base_price
