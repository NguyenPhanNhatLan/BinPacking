def evaluate_population(population, items, container):
    fitness_scores = []
    for individual in population:
        total_volume = 0
        total_weight = 0
        total_value = 0
        bonus = 0
        for i in individual:
            item = items[i]
            total_volume += item.volume
            total_weight += item.weight
            total_value += item.value
            bonus += item.priority
            if item.fragile:
                bonus += 2
            if item.sensitive:
                bonus += 1
        if total_volume > container.volume or total_weight > container.max_weight:
            fitness_scores.append(0)
        else:
            fitness_scores.append(total_value + bonus)
    return fitness_scores