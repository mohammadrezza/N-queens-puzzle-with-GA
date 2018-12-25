import random

NUMBER_OF_QUEENS = 8
PRIMITIVE_POPULATION = 50
MUTATE_RATIO = 0.1


class Situation:
    def __init__(self):
        self.ordering = []
        self.chance = None

    def __mul__(self, other):
        l = []
        for _ in range(other):
            sit = Situation()
            sit.__dict__ = self.__dict__
            l.append(sit)
        return l


def create_population():
    crowd = []
    # indexes represents column number
    for i in range(PRIMITIVE_POPULATION):
        sit = Situation()
        # value of the indexes represents row number
        for j in range(NUMBER_OF_QUEENS):
            sit.ordering.append(random.randrange(NUMBER_OF_QUEENS))
        crowd.append(sit)
    return crowd


def order(k):
    # calculating all possible hit situations
    return int(k * (k - 1) / 2)


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
        crowd[i].chance = order(NUMBER_OF_QUEENS) - evaluate(crowd[i].ordering)
    return crowd


def selection(crowd):
    pot = []
    for prsn in crowd:
        pot.extend(prsn * prsn.chance)
    return random.sample(pot, PRIMITIVE_POPULATION)

def cross_over(crowd):
    child = []
    for i in range(0, len(crowd), 2):
        father = crowd[i].ordering
        mother = crowd[i + 1].ordering
        cross_point = random.randrange(0, NUMBER_OF_QUEENS)
        boy = Situation()
        girl = Situation()
        boy.ordering = father[:cross_point] + mother[cross_point:]
        girl.ordering = mother[:cross_point] + father[cross_point:]
        child.append(boy)
        child.append(girl)
    return child

def mutation(child):
    for i, children in enumerate(child):
        rnd = round(random.uniform(0.0, 1.0), 2)
        if rnd < MUTATE_RATIO:
            queen = random.randrange(0, NUMBER_OF_QUEENS)
            pos = random.randrange(0, NUMBER_OF_QUEENS)
            children.ordering[queen] = pos
    return child


population = create_population()

condition = True
while condition:
    fitted_population = fitness(population)
    parents = selection(fitted_population)
    mutation(cross_over(parents))
