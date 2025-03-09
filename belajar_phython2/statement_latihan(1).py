# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Masukkan sebuah kata = ")

for letter in userWord:
    if letter.upper() in ['A','I','U','E','O']:
        continue
    
    print(letter.upper())