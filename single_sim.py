import numpy as np
from random import choices
import matplotlib.pyplot as plt
from itertools import combinations

########
# summary of the entire code.
# You have a no of policies you want to make a decision about (say 2 ) , you are lets say 10 people
# so 10 voters in total. In the code you will store all possible distinct decisions you can have to
# to a policy. In our example we will have [ Y Y ], [ Y N ], [ N Y ], [ N N ] , this is dd. Now you
# Now you can assume ( the first case ) , each decision vector ( ex [ Y Y ] ) has a equal probability
# of being expressed in the voter population. Each person is also equally likely to be chosen as a
# representative. In the code an overlap matrix has been constructed which for each decision vector
# checks the overlap with another decision vector ( ex [ Y Y ] and [ Y N ]  have 1 overlap.
# How is a party defined? IF there are let us say 3 parties and 2 policies then we will take
# all ways to have 3 parties choosing from 4 distinct policy vectors i.e 4 choose 3
# After this we just see which party has maximum overlap with all the other voter"s decision vectors.

#########
Nd = 2  # This is the number of topic to have a decision about
Np = 2  # This is the number of parties
Nv = 10  # This is the number of voters

dd = 2 ** Nd  # Distinct decision vectors

prob = np.ones(dd)  # Probability measure over the opinions
prob /= np.sum(prob)

voter_vec = choices(np.arange(0, dd), prob, k=Nv)
# Each element represents the perspective of the corresponding voter
### voter_vec has length 100 and each element is a number between 0 and dd which
## comes from a uniform distribution over 0 and dd

dec_arr = np.zeros((dd, Nd), dtype=int)  # Decision array has all the dd's
voter_arr = np.zeros((Nv, Nd), dtype=int)  # Voter Decision array
### voter_arr is just binary representation of voter_vec

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
    print("voter", voter_vec)
    comp = ovl_mat[x]  # The fighting parties
    counter = np.zeros(len(x))

    for i in range(Nv):
        listy = comp[:, voter_vec[i]]
        winner = np.argwhere(listy == np.amax(listy)).flatten()
        counter[winner] += 1. / len(winner)

    return counter


parties = np.array([0, 1, 6], dtype=int)

print(winner_rep(parties, voter_vec))


def direct_democracy(voter_vector):
    total = np.zeros(dd)
    best_policies = []
    freq = np.zeros(dd)
    for a in range(dd):
        freq[a] = np.count_nonzero(voter_vector == a)
    for a in range(dd):
        for b in range(dd):
            ovl_mat[a, b] = np.count_nonzero(dec_arr[a] == dec_arr[b])
    max_value = np.dot(ovl_mat[0, :], freq)
    print("oval",ovl_mat[0, :] )
    print("freq", freq)
    for c in range(dd):
        total[c] = np.dot(ovl_mat[c, :], freq)
        if total[c] >= max_value:
            max_value = total[c]
    for d in range(dd):
        if total[d] == max_value:
            best_policies.append(d)
    return best_policies


direct_democracy(np.array([0, 2, 1, 1, 0, 3, 1, 3, 0, 0]))


def representative_democracy(Nd1, Np1, Nv1):
    dd1 = 2 ** Nd1  # Distinct decision vectors
    representatives = np.zeros(Np1)
    prob1 = np.ones(dd1)  # Probability measure over the opinions
    prob1 /= np.sum(prob1)

    voter_vec1 = choices(np.arange(0, dd1), prob1, k=Nv1)
    new_arrays = np.array_split(voter_vec1, Np1, axis=0)
    for a in range(len(new_arrays)):
        print("dd", direct_democracy(new_arrays[a]))
        representatives[a] = direct_democracy(new_arrays[a])[0]
    print("rep", representatives)
    winner = winner_rep(representatives, voter_vec1)
    print("winner", winner)


representative_democracy(2, 3, 10)
