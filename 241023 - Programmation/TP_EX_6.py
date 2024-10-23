from pycparser.c_ast import While


def average_temperature(numbers_list: list[int]):
    """Calcule la moyenne des nombres donné

    Parameters
    ----------
    numbers_list : liste des températures donnée par le joueur (list[int])

    Returns
    -------
    Result: la moyenne des nombres entré
    """
    total_number = 0

    for number in numbers_list:
        total_number += number

    return total_number / len(numbers_list)


temperature_list = []

while True:

    player_input = input("Enter a Temperature: ")
    try:
        input_number = int(player_input)

        if input_number == -100:
            print("Stopped adding temperatures.")
            break

        else:
            temperature_list.append(input_number)
            print("Value added.")

    except:
        print("Invalid input")

average = average_temperature(temperature_list)
amount_temp = len(temperature_list)

print(f"The {amount_temp} last day's average temperature was: {average}")



