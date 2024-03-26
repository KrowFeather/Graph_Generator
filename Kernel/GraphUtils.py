from random import random
import GraphBuffer as GB


def random_edges():
    u = random.randint(1, GB.MAX_NODE_SIZES + 1)
    v = random.randint(1, GB.MAX_NODE_SIZES + 1)
    weight = random.randint(1, 10)
    return u, v, weight
