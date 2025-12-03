import re

with open("input.txt") as f:
    ranges = f.read().strip().split(",")

invalids = []

for rng in ranges:
    low, high = rng.split("-")[0], rng.split("-")[1] # split the range into a low and a high number
    
    nums = range(int(low), int(high) + 1)
    for n in nums:
        n = str(n)
        if n[:len(n) // 2] == n[len(n) // 2:]: # the problem only requires a simple check to see if the two halves are the same
            invalids.append(int(n))
            break

print(sum(invalids))