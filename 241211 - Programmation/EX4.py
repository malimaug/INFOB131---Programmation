def vowel_amount(word: str) -> int:

    if word == "":
        print("Empty string")
        return 0, 0, 0, 0, 0, 0

    else:
        iterate_vowel = vowel_amount(word[1:])

        a, e, i, o, u, y = iterate_vowel

        if word[0] == 'a':
            a += 1

        elif word[0] == 'e':
            e += 1

        elif word[0] == 'i':
            i += 1

        elif word[0] == 'o':
            o += 1

        elif word[0] == 'u':
            u += 1

        elif word[0] == 'y':
            y += 1

        return a, e, i, o, u, y

print(vowel_amount("hello, my name is matteo the great"))