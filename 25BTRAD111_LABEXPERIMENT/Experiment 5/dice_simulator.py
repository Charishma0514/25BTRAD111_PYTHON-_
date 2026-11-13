import random

count = int(input("Enter number of dice rolls: "))

for i in range(count):
    result = random.randint(1, 6)
    print("Dice result:", result)
