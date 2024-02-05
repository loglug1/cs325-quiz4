import random

def scramble(x: str):
    for i in range(0,9):
        split_index = random.randint(0,len(x)-1)
        parts = x.split(x[split_index], 1)
        x = parts[1] + x[split_index] + parts[0]
    return x