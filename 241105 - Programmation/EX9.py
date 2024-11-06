def vowel_amount(word:str)->int:
    """
    the function tells how many vowels are in a string

    Parameters
    ----------
    word: the analysed string (str)

    Return
    ------
    result: the amount of vowels in the string (int)
    """
    vowel_count = 0

    for character in word:
        if character in 'aeiouy':
            vowel_count += 1

    return vowel_count