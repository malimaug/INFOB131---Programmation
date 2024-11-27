
def create_mountain_dictionary():
    """Reads mountain.txt and returns a dictionary of each peak and its characteristics.

    Returns
    -------
    mountains : the dictionary containing the peaks and their characteristics.
    """

    file = open('mountains.txt', 'r')
    lines_list = file.readlines()
    file.close()

    mountains = {}

    for line in lines_list:

        line = line.strip()
        line = line.split('; ')

        line[2] = line[2][:-1]

        mountains[line[0]] = (line[1], line[2])

    return mountains

print(create_mountain_dictionary())