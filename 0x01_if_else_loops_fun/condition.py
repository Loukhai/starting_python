import random

number = random.randint(-10, 10)

if number < 0:
    print(f"{number} negative")
elif number > 0:
    print(f"{number} positive")
else:
    print(f"{number} it's 💀")
