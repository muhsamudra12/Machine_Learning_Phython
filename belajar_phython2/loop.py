#1
for i in range(1, 11):
    if i % 2 !=0:
        print(i,end=' ')

#2
x=1
while x<11:
    if x % 2 !=0:
        print(x,end=' ')
    x +=1

#3
for ch in "ratna.lestari@ugm.ac.id":
    if ch == "@":
        break
    print(ch,end=' ')

#4
for digit in "0165031806510":
    if digit == "0": 
        print ("x")
        continue
    print(digit)