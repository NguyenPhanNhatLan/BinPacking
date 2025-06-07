import random

def crossover(parents, config):
    children = []
    for i in range(0, len(parents), 2):
        p1 = parents[i]
        p2 = parents[i+1 if i+1 < len(parents) else 0]
        cut = random.randint(1, min(len(p1), len(p2)) - 1)
        child1 = p1[:cut] + p2[cut:]
        child2 = p2[:cut] + p1[cut:]
        children.extend([child1, child2])
    return children