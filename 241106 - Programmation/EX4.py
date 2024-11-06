def is_valid_DNA(dna_string) -> bool:
    """
    The function tells if a string is a valid ADN encoding or not

    Parameters
    ----------
    dna_string : the string containing the DNA encoding (str)

    Returns
    -------
    result : True if the string is valid, False if not
    """

    for character in dna_string:
        if character not in ["A","T","G","C"]:
            return False

    return True

def distinct_occurences(sequence: str, subsequence: str):
    """counts all distinct occurences of a subsequence of DNA in a full sequence of DNA

    Parameters
    ----------
    sequence : the given DNA sequence(str)
    subsequence : the given DNA subsequence we want to detect (str)

    Returns
    -------
    result : the amount of distinct occurences of the subsequence (int)
    """
    sequence_position = 0
    occurences = 0
    while sequence_position < len(sequence):
        if sequence[sequence_position:(sequence_position + len(subsequence))] == subsequence:
            occurences += 1
            sequence_position += len(subsequence)
        else:
            sequence_position += 1

    return occurences

def total_occurences(sequence: str, subsequence: str):
    """counts all the occurences of a subsequence of DNA in a full sequence of DNA

    Parameters
    ----------
    sequence : the given DNA sequence(str)
    subsequence : the given DNA subsequence we want to detect (str)

    Returns
    -------
    result : the amount of distinct occurences of the subsequence (int)
    """
    sequence_position = 0
    occurences = 0
    while sequence_position < len(sequence):
        if sequence[sequence_position:(sequence_position + len(subsequence))] == subsequence:
            occurences += 1

        sequence_position += 1

    return occurences

DNA = "ATGCATGCATGCATGCATAGCACACGTACTGCTAGCTGATCGATGAGTCGATCGATC"
DNA_sub = "ATGCATGC"

occurences = distinct_occurences(DNA, DNA_sub)

proportion = occurences*len(DNA_sub) / len(DNA)


print(occurences, proportion)
print(total_occurences(DNA, DNA_sub))


print("%.2f%% of your chain is composed of \"%s\"" % (proportion*100, DNA_sub))
