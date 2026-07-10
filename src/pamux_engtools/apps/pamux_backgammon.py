import random

seed = input("Enter seed...")

random.seed(seed)

while True:
    print(f"{random.randint(1, 6)}-{random.randint(1, 6)}")
    input("Press Enter to continue...")
