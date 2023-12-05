'''
Created on Dec 4, 2023

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both
7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set
of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
from datetime import datetime

import networkx as nx
from tqdm import trange, tqdm

from euler import is_prime_list, is_prime


def concat_nums(a, b):
    return int(str(a) + str(b)), int(str(b) + str(a))


if __name__ == '__main__':
    start = datetime.now()

    max_val = 10_000
    clique_size = 5

    prime_list = is_prime_list(max_val)
    just_primes = [idx for idx, prime in enumerate(prime_list) if prime]
    num_primes = len(just_primes)

    prime_graph = nx.Graph()

    for i in trange(num_primes - 1, position=0):
        for j in trange(i + 1, num_primes, position=1, leave=False):
            a = just_primes[i]
            b = just_primes[j]
            ab, ba = concat_nums(a, b)
            if is_prime(ab) and is_prime(ba):
                prime_graph.add_edge(a, b)

    # Find cliques (maximal connected subgraph)
    cliques = list(nx.find_cliques(prime_graph))
    cliques = []
    for n in tqdm(prime_graph.nodes):
        if len(list(prime_graph.neighbors(n))) >= clique_size:
            cliques.extend(list(nx.find_cliques(prime_graph, nodes=[n,])))
    print(f'{len(cliques)} cliques found')

    max_cliques = [clique for clique in cliques if len(clique) == clique_size]
    min_sum_clique = min(max_cliques, key=lambda x: len(x)) if len(max_cliques) > 0 else []
    print(min_sum_clique)
    print(sum(min_sum_clique))

    end = datetime.now()
    print(f'\nruntime = {end - start}')
