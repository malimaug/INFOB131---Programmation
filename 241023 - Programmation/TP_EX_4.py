def dividers(number: int):
    """Displays the dividers and the amount of them

    Parameters
    ----------
    number : the number we want to find the dividers from (int)

    """
    divider_list = []

    for div in range(1, number+1):
        if number % div == 0:
            divider_list.append(div)

    print(f"There are {len(divider_list)} dividers")
    print(f"The dividers are: {str(divider_list)}")

try:
    player_number = int(input("Enter a number: "))
    if player_number > 0:
        dividers(player_number)

except:
    print("Number not valid")

