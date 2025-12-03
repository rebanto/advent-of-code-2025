import re

with open("input.txt") as f:
    ranges = f.read().strip().split(",")

invalids = []

for rng in ranges:
    low, high = rng.split("-")[0], rng.split("-")[1] # split the range into a low and a high number
    
    nums = range(int(low), int(high) + 1)
    for n in nums:
        n = str(n)
        
        for i in range(1, len(n) // 2 + 1): # get each substring up to half the string
            pot = n[:i]
            
            if len(n) % len(pot) == 0: # check if the substring repeated fits the length of string
                if n == pot * (len(n) // len(pot)): # if the string can be reconstructed with substring
                    invalids.append(int(n))
                    break

print(sum(invalids))