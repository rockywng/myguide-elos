import random

if __name__ == "__main__":
    # try some random head to heads and see what happens!
    # try with 10 restaurants
    win_probabilities = {}
    for i in range(10):
        for j in range(10):
            win_probabilities[tuple([i, j])] = random.uniform(0, 1)
    
    print(win_probabilities)

    for _ in range(1000):
        # pick random i and j
        i = random.randint(0, 10)
        j = random.randint(0, 10)
        while j == i:
            j = random.randint(0, 10)
        