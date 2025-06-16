
nums = [3,4,2,2,3,4,7,9,7,9,4,5,6,1,5,6,4]
frequency = {}

for num in nums:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)