def tournament_selection(population, fitness_scores, k=3):
    import random
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness_scores)), k)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected.append(winner)
    return selected
