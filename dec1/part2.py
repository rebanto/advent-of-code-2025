with open("input.txt", "r") as file:
    content = file.readlines()

total_zero_hits = 0
current_dial_position = 50

for line in content:
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])
    
    P_start = current_dial_position
    
    if direction == "R":
        # right rotation hits 0 whenever the total displacement is a multiple of 100
        zero_hits = (P_start + distance) // 100
        
        # calculate the final position
        current_dial_position = (P_start + distance) % 100
    elif direction == "L": # different logic for left - took me a while to figure out...
        C0 = P_start if P_start != 0 else 100 # clicks to reach the first 0
        
        if distance < C0:
            zero_hits = 0
        else:
            # 1 hit at C0, and 1 more hit for every 100 clicks left
            remaining_distance = distance - C0
            zero_hits = 1 + (remaining_distance // 100)  
            
        current_dial_position = (P_start - distance) % 100
        
    total_zero_hits += zero_hits

print(total_zero_hits)