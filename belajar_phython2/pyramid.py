blocks = int(input("Enter the number of blocks: "))
current_block = 0
height = 0
i=0

while i<blocks:
    height += 1
    current_block += height
    # print(i,current_block)
    if current_block> blocks:
        break

height -= 1

print("The height of the pyramid:", height)