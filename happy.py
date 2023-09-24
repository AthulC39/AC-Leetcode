message = input("")
happy = 0
sad = 0


for i in range(0, len(message)):
    if i+2<len(message):
        if (message[i] == ":") and (message[i + 1]) == "-" and (message[i + 2]) == ")":
            happy += 1
        elif (message[i]) == ":" and (message[i + 1] == "-") and (message[i + 2] == "("):
            sad += 1


if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif sad == happy and happy > 0:
    print("unsure")
else:
    print("none")