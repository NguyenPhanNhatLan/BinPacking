# core/ga/run_ga.py
from core.optimizer import Optimizer
from .population import initialize_population
from .selection import tournament_selection
from .crossover import crossover
from .mutation import mutate
from .fitness import evaluate_population

class GAOptimizer(Optimizer):
    def optimize(self, items, container, config):
        population = initialize_population(items, config['population_size'])

        for gen in range(config['generations']):
            fitness_scores = evaluate_population(population, items, container)
            selected = tournament_selection(population, fitness_scores)
            offspring = crossover(selected, config)
            mutated = mutate(offspring, config)
            population = mutated

        best_individual = max(population, key=lambda ind: evaluate_population([ind], items, container)[0])
        return best_individual
