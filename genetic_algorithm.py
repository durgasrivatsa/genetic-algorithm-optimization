import random

def fitness(individual):
    return sum(individual)

def create_individual(size):
    return [random.randint(0, 1) for _ in range(size)]

def create_population(size, individual_size):
    return [create_individual(individual_size) for _ in range(size)]

def selection(population):
    return max(population, key=fitness)

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def mutation(individual, rate=0.01):
    return [gene if random.random() > rate else 1 - gene for gene in individual]

def genetic_algorithm(pop_size=20, ind_size=10, generations=100):
    population = create_population(pop_size, ind_size)
    for gen in range(generations):
        new_population = []
        for _ in range(pop_size):
            p1 = selection(random.sample(population, 5))
            p2 = selection(random.sample(population, 5))
            child = mutation(crossover(p1, p2))
            new_population.append(child)
        population = new_population
        best = selection(population)
        print(f"Generation {gen+1}: Best fitness = {fitness(best)}")
    return selection(population)

result = genetic_algorithm()
print("Best solution:", result)
