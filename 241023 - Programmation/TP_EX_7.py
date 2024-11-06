def player_input_to_list():
    """
    Function asks the user to input a list of numbers

    Returns
    -------
    result: list of inputed numbers
    """
    number_list = []

    while True:
        user_input = input("Enter a number: ")
        number_input = int(user_input)
        if number_input >= 0:
            number_list.append(number_input)

        elif number_input == -1:
            print("Made List")
            break

        else:
            print("Invalid Input")

    return number_list


def find_max_in_list(list: list[int]):
    """
    Function finds the maximum value in a list

    Parameters
    ----------
    list: list of integers (list[int])

    Returns
    -------
    result:
    """
    highest_found = max(list)
    amount_found = 0

    for number in list:
        if number == highest_found:
            amount_found += 1

    return highest_found, amount_found


def find_min_in_list(list: list[int]):
    """
    Function finds the minimum value in a list

    Parameters
    ----------
    list: list of integers (list[int])

    Returns
    -------
    result:
    """
    lowest_found = min(list)
    amount_found = 0

    for number in list:
        if number == lowest_found:
            amount_found += 1

    return lowest_found, amount_found



number_list = [2,2,3,4,4,4,45,45,45,45,1,1,1,1,1]

max_return = find_max_in_list(number_list)
print(max_return[0], f"is the highest number,{max_return[1]} available in the list")

min_return = find_min_in_list(number_list)
print(min_return[0], f"is the highest number,{min_return[1]} available in the list")
