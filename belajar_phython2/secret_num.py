secretNum = 777

guessNum = 0

while guessNum != secretNum:
    guessNum = int(input("Input angka rahasia untuk berhenti : "))
    if guessNum != secretNum:
        print("Perulangan akan terus lanjut...")

print("Well done, Congrats...")