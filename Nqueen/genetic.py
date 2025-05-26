import random

def solve_n_queens_genetic(nq):
    def random_chromosome(size):
        return [random.randint(0, nq - 1) for _ in range(nq)]

    def fitness(chromosome):
        horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2
        diagonal_collisions = 0
        n = len(chromosome)
        left_diagonal = [0] * 2 * n
        right_diagonal = [0] * 2 * n
        for i in range(n):
            left_diagonal[i + chromosome[i] - 1] += 1
            right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1
        diagonal_collisions = 0
        for i in range(2 * n - 1):
            counter = 0
            if left_diagonal[i] > 1:
                counter += left_diagonal[i] - 1
            if right_diagonal[i] > 1:
                counter += right_diagonal[i] - 1
            diagonal_collisions += counter / (n - abs(i - n + 1))
        return int(maxFitness - (horizontal_collisions + diagonal_collisions))

    def probability(chromosome):
        return fitness(chromosome) / maxFitness

    def random_pick(population, probabilities):
        total = sum(probabilities)
        r = random.uniform(0, total)
        upto = 0
        for chromo, prob in zip(population, probabilities):
            if upto + prob >= r:
                return chromo
            upto += prob
        return population[0]  # fallback

    def reproduce(x, y):
        n = len(x)
        c = random.randint(0, n - 1)
        return x[0:c] + y[c:n]

    def mutate(x):
        n = len(x)
        c = random.randint(0, n - 1)
        m = random.randint(0, n - 1)
        x[c] = m
        return x

    def genetic_queen(population):
        mutation_probability = 0.03
        new_population = []
        probabilities = [probability(n) for n in population]
        for i in range(len(population)):
            x = random_pick(population, probabilities)
            y = random_pick(population, probabilities)
            child = reproduce(x, y)
            if random.random() < mutation_probability:
                child = mutate(child)
            print("Chromosome = {},  Fitness = {}".format(str(child), fitness(child)))
            new_population.append(child)
            if fitness(child) == maxFitness:
                break
        return new_population

    maxFitness = (nq * (nq - 1)) / 2
    population = [random_chromosome(nq) for _ in range(100)]
    generation = 1

    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population)
        print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        print("")
        generation += 1

    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("Solved in Generation {}!".format(generation - 1))
            print("One of the solutions:")
            print("Chromosome = {},  Fitness = {}".format(str(chrom), fitness(chrom)))
            return chrom

    return None
