with open("input.txt", "r") as file:
    content = file.readlines()

num = 0
dial = 50

for line in content:
    change = int(line[1:]) 
    
    # apply rotation
    if line[0] == "R":
        dial += change
    else: 
        dial -= change
    
    # use modulo 100 to get the final position since dial wraps around 0-99
    dial %= 100

    if dial == 0:
        num += 1

print(num)