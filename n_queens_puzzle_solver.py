import random

NUMBER_OF_QUEENS = 8
PRIMITIVE_POPULATION = 50


def create_population():
    crowd = []
    # indexes represents column number
    for i in range(PRIMITIVE_POPULATION):
        rnd = []
        # value of the indexes represents row number
        for j in range(NUMBER_OF_QUEENS):
            rnd.append(random.randrange(NUMBER_OF_QUEENS))
        crowd.append(rnd)
    return crowd


def order(k):
    # calculating all possible hit situations
    return k * (k - 1) / 2


def evaluate(number):
    hit = 0
    for i in range(NUMBER_OF_QUEENS):
        for j in range(i, NUMBER_OF_QUEENS):
            if i == j:
                continue
            row_diff = abs(number[i] - number[j])
            col_diff = abs(i - j)
            if row_diff == 0:  # the queens are in the same row
                hit += 1
            elif row_diff == col_diff:  # the queens are diagonal
                hit += 1
    return hit


def fitness(crowd):
    for i in range(len(crowd)):
        crowd[i] = [crowd[i], int(order(NUMBER_OF_QUEENS)) - evaluate(crowd[i])]
    return crowd


population = create_population()
print(fitness(population))
