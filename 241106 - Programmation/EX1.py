char_to_morse = {'a':'.-',
                 'b':'-...',
                 'c':'-.-.',
                 'd':"-..",
                 'e':".",
                 'f':"..-.",
                 'g':"--.",
                 'h':"....",
                 'i':"..",
                 'j':".---",
                 'k':"-.-",
                 'l':".-..",
                 'm':"--",
                 'n':"-.",
                 'o':"---",
                 'p':".--.",
                 'q':"--.-",
                 'r':".-.",
                 's':"...",
                 't':"-",
                 'u':"..-",
                 'v':"...-",
                 'w':".--",
                 'x':"-..-",
                 'y':"-.--",
                 'z':"--..",
                 ' ':"  "}

word = input("Enter a word: ")
morse_word = ""

for letter in word:
    morse_word += (char_to_morse[letter] + " ")

print(morse_word)