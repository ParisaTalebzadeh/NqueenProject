import numpy as np
import random

def check_fitness(population: np.ndarray) -> np.ndarray:
    pop_size, n = population.shape
    fitness = np.zeros(pop_size, dtype=int)
    for idx, solution in enumerate(population):
        conflicts = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(solution[i] - solution[j]) == abs(i - j):
                    conflicts += 1
        fitness[idx] = conflicts
    return fitness

def tournament_selection(pop: np.ndarray,
                         fit: np.ndarray,
                         k: int = 3) -> np.ndarray:
    pop_size = pop.shape[0]
    candidates = np.random.choice(pop_size, size=k, replace=False)
    best = candidates[0]
    for idx in candidates[1:]:
        if fit[idx] < fit[best]:
            best = idx
    return pop[best].copy()

def order_crossover(parent1: np.ndarray,
                    parent2: np.ndarray,
                    cut_length: int) -> (np.ndarray, np.ndarray):
    n = parent1.shape[0]
    child1 = np.full(n, -1, dtype=int)
    child2 = np.full(n, -1, dtype=int)

    start = random.randint(0, n - cut_length)
    end = start + cut_length

    child1[start:end] = parent1[start:end]
    child2[start:end] = parent2[start:end]

    def fill_remaining(child: np.ndarray, donor: np.ndarray):
        idx_fill = 0
        for gene in donor:
            if gene not in child:
                while child[idx_fill] != -1:
                    idx_fill += 1
                child[idx_fill] = gene
        return child

    child1 = fill_remaining(child1, parent2)
    child2 = fill_remaining(child2, parent1)
    return child1, child2

def swap_mutation(chromosome: np.ndarray,
                  num_swaps: int = 1) -> np.ndarray:
    child = chromosome.copy()
    n = child.shape[0]
    for _ in range(num_swaps):
        i, j = np.random.choice(n, size=2, replace=False)
        child[i], child[j] = child[j], child[i]
    return child

def solve_n_queens_genetic(n: int,
                           pop_size: int = 500,
                           generations: int = 2500,
                           p_mutation: float = 0.2,
                           tournament_k: int = 3,
                           cut_length: int = 2,
                           num_swaps: int = 1,
                           elitism: bool = True) -> list:

    population = np.zeros((pop_size, n), dtype=int)
    for i in range(pop_size):
        population[i, :] = np.random.permutation(n)

    fitness = check_fitness(population)

    for gen in range(1, generations + 1):
        print(f"\n========== Generation {gen} Chromosomes ==========")
        for sol in population:
            print(sol.tolist())

        best_idx = np.argmin(fitness)
        best_solution = population[best_idx].copy()
        best_conflicts = int(fitness[best_idx])
        print(f"\n>>> Generation {gen}: Best conflicts = {best_conflicts} | Board = {best_solution.tolist()}")

        if best_conflicts == 0:
            print("\n solution found!")
            return (best_solution + 1).tolist()

        new_population = []
        if elitism:
            new_population.append(best_solution.copy())

        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitness, tournament_k)
            parent2 = tournament_selection(population, fitness, tournament_k)
            child1, child2 = order_crossover(parent1, parent2, cut_length)
            if random.random() < p_mutation:
                child1 = swap_mutation(child1, num_swaps)
            if random.random() < p_mutation:
                child2 = swap_mutation(child2, num_swaps)
            new_population.append(child1)
            if len(new_population) < pop_size:
                new_population.append(child2)

        population = np.vstack(new_population)
        fitness = check_fitness(population)

    best_idx = np.argmin(fitness)
    print("\n Returning best found:")
    final_best = population[best_idx]
    return (final_best + 1).tolist()
