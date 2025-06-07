def mutate(population, config):
    import random
    mutation_rate = config.get('mutation_rate', 0.05)
    for individual in population:
        if random.random() < mutation_rate:
            if len(individual) > 1:
                i, j = random.sample(range(len(individual)), 2)
                individual[i], individual[j] = individual[j], individual[i]
    return population