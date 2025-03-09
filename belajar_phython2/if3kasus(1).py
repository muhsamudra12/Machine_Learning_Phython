num1 = int(input("First Number : "))
num2 = int(input("Second Number : "))
num3 = int(input("Third Number : "))

#set number1 sebagai yang terbesar
largestNum = num1

#deteksi apakah num2 > num1
if num2 > largestNum:
    largestNum = num2

#deteksi apakah num3 > num2
if num3 > largestNum:
    largestNum = num3

print("The largest number is: ", largestNum)