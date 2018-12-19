import random

NUMBER_OF_QUEENS = 8
PRIMITIVE_POPULATION = 50


def create_population():
    crowd = []
    for i in range(PRIMITIVE_POPULATION):
        rnd = []
        for j in range(NUMBER_OF_QUEENS):
            rnd.append(random.randrange(NUMBER_OF_QUEENS))
        crowd.append(rnd)
    return crowd


print(create_population())
