word = input()
counter = word.count("B")
word = word.replace("B", "") + " "
Left = True

for i in word:
    if Left:
        if word[:2] == "LL":
            counter += 1
            Left = False
            word = word[2:]

        elif word[:2] == "LR":
            counter += 1
            word = word[1:]

        elif word[0] == "R":
            word = word[1:]

        elif word[:2] == "L " or word[0] == " ":
            counter += 1
            break

    if not Left:
        if word[:2] == "RR":
            counter += 1
            Left = True
            word = word[2:]

        elif word[:2] == "RL" or word[0] == "R":
            counter += 1
            word = word[1:]

        elif word[0] == "L":
            word = word[1:]

print(counter)
