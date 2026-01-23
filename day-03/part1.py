from heapq import heappop, heappush, heapify

filepath = "example.txt"
totalJoltage = 0

with open(filepath, "r") as file:
    for line in file:

        maxDigitSeen = 0
        lineMaxJoltage = 0

        for char in line.strip():
            currentDigit = int(char)

            if maxDigitSeen != 0:
                combination = maxDigitSeen * 10 + currentDigit
                lineMaxJoltage = max(lineMaxJoltage, combination)

            maxDigitSeen = max(maxDigitSeen, currentDigit)

        totalJoltage += lineMaxJoltage

assert totalJoltage == 357, f"expected 357, got {totalJoltage}"
print(f"Total Joltage: {totalJoltage}")
