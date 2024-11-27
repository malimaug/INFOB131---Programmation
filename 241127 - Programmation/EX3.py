import pickle
import os

"""
data_structure = [('nom', 'R2D2'), ('age', 42), ('prenom', 'Z-6PO')]

file = open('codedata_structure.pkl', 'wb')
pickle.dump(data_structure, file)
file.close()
"""

def read_file(filename: str) -> list:
    """The function reads a pickle file and returns the data it contains

    Parameters
    ----------
    filename : the name of the fil ewe want to read. (str)

    Returns
    -------
    data : the list from the file (list)
    """

    file = open(filename, 'rb')
    data = pickle.load(file)
    file.close()

    return data


def list_to_dict(data: list) -> dict:
    """The function converts a list to a dictionary.

    Parameters
    ----------
    data : the list from the file (list)

    Returns
    -------
    dictionary : the reorganised data into a dictionary (dict)
    """

    dictionary = {}

    for tuple_data in data:

        dictionary[tuple_data[0]] = tuple_data[1]


    return dictionary


def store_dict(dictionary: dict):
    """The function stores a dictionary into a pickle file.

    Parameters
    ----------
    dictionary : the reorganised data into a dictionary (dict)
    """

    if not os.path.exists('dico'):
        os.mkdir('dico')

    file = open('dico/my_dico.pkl', 'wb')
    pickle.dump(dictionary, file)
    file.close()


#testing

data = read_file('codedata_structure.pkl')
dictionary = list_to_dict(data)
store_dict(dictionary)

file = open('dico/my_dico.pkl', 'rb')
dictionary = pickle.load(file)
file.close()

print(dictionary)