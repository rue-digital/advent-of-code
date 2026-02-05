## Defining the Problem

```The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)```


## Solutions

### Brute Force

For each bank (line file), loop through the digits with two nested loops to calculate every possible combination of joltage. At each iteration, update the current maximum. Once reaching the end of the bank, add the maximum joltage of the bank to the total joltage. Repeat until end of file.

time complexity: O(n^2) space complexity: O(1)

### Two pointers

For each bank, store the maximum digit previously encountered and the maximum joltage of the line. Iterate through the bank. If the maxDigitSeen is not none, calculate the combined joltage of the maxDigitSeen and the current digit value. Update maximum joltage of the bank if necessary. Update maxDigitSeen if current digit is greater. Once reaching the end of the bank, add the joltage of the bank to the total joltage. Repeat until end of file.

time complexity: O(n) space complexity: O(1)