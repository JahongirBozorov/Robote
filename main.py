def Robot(yonalish: str, joy: list):
    yonalish = list(yonalish)
    dict1 = {"O": "O'ngga", "C": "Chapga", "T": "To'g'riga"}
    for i in yonalish:
        if i == "T":
            joy[0] += 1
        elif i == "O":
            joy[1] += 1
        elif i == "C":
            joy[1] -= 1
    return f"{joy}+Joylashgan va + {dict1[yonalish[-1]]} ga qarab turipti"
print(Robot("TTOOCOTCO", [5, 7]))



