import numpy as np
from random import choices
import matplotlib.pyplot as plt
from itertools import combinations

Nd = 3  # This is the number of topic to have a decision about
Np = 2  # This is the number of parties
Nv = 100  # This is the number of voters

dd = 2 ** Nd  # Distinct decision vectors

prob = np.ones(dd)  # Probability measure over the opinions
prob /= np.sum(prob)

voter_vec = choices(np.arange(0, dd), prob, k=Nv)
# Each element represents the perspective of the corresponding voter

dec_arr = np.zeros((dd, Nd), dtype=int)  # Decision array has all the dd's
voter_arr = np.zeros((Nv, Nd), dtype=int)  # Voter Decision array

for i in range(dd):
    dec_arr[i] = np.array(list(np.binary_repr(i, width=Nd)), dtype=int)

for i in range(Nv):
    voter_arr[i] = dec_arr[voter_vec[i]]

## Now we make the overlap matrix

ovl_mat = np.zeros((dd, dd), dtype=int)

for i in range(dd):
    for j in range(dd):
        ovl_mat[i, j] = np.count_nonzero(dec_arr[i] == dec_arr[j])


## Given Np parties find the one that wins according to representative democ.

def winner_rep(x, voter_vec):
    comp = ovl_mat[x]  # The fighting parties
    counter = np.zeros(len(x))

    for i in range(Nv):
        listy = comp[:, voter_vec[i]]
        winner = np.argwhere(listy == np.amax(listy)).flatten()
        counter[winner] += 1. / len(winner)

    return counter


parties = np.array([0, 1, 6], dtype=int)

print(winner_rep(parties, voter_vec))

counter = np.zeros(len(parties))

for i in range(1000):
    np.random.seed()
    vv = choices(np.arange(0, dd), prob, k=Nv)
    ans = winner_rep(parties, vv)

    winners = np.argwhere(ans == np.amax(ans)).flatten()
    counter[winners] += 1. / len(winners)

print(counter)



