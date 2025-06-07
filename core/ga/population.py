import random

def initialize_population(items, population_size):
    population = []
    for _ in range(population_size):
        individual = []
        for i, item in enumerate(items):
            quantity = random.randint(0, item.quantity)
            individual.extend([i] * quantity)
        random.shuffle(individual)
        population.append(individual)
    return population