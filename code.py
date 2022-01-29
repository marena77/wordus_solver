import re

def getGuessResults(guess):
    letters = []
    for i in range(0,5):
        color = input("Color of letter number " + str(i) + "? (black/yellow/green):")
        letters.append((guess[i],color,i))
    return letters

def formRE(guessResults):
    char_list = ["[","[","[","[","["]
    yellow_list = []
    for (letter,color,index) in guessResults:
        if color == "black":
            for i in range(0,5):
                char_list[i] = char_list[i] + "^" + letter
        if color == "yellow":
            for i in range(0,5):
                if i == index:
                    char_list[i] = char_list[i] + "^" + letter
                else:
                    char_list[i] = char_list[i] + letter
            yellow_list.append(re.compile(letter + "+"))
    for i in range(0,5):
        char_list[i] = char_list[i] + "]"
    for (letter,color,index) in guessResults:
        if color == "green":
            char_list[index] = "[" + letter + "]"
    return "".join(char_list), yellow_list

def getYellowRE(letter):
    return re.compile(letter + "+")


f = open("sgb-words.txt")
words = set()

for line in f.readlines():
    words.add(line[:5])

guesses = 0
re_list = []
while guesses < 6:
    if guesses == 0:
        guess = input("First guess: ")
    else:
        guess = input("What will you guess: ")
    guesses += 1

    l = getGuessResults(guess)
    main_re, yellow_list = formRE(l)
    re_list.append(re.compile(main_re))
    re_list = re_list + yellow_list
    print(re_list)

    for word in words:
        flag = True
        for i in range(0,len(re_list)):
            if re_list[i].match(word) and (i == len(re_list)-1) and flag:
                print("Try guessing: " + word)
            if not re_list[i].match(word):
                flag = False
