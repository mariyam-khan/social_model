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
# After this we jst see which party has maximum overlap with all the other voter"s decision vectors.

#########
Nd = 3  # This is the number of topic to have a decision about
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

counter = np.zeros(len(parties))

for i in range(10):
    np.random.seed()
    vv = choices(np.arange(0, dd), prob, k=Nv)
    ans = winner_rep(parties, vv)

    winners = np.argwhere(ans == np.amax(ans)).flatten()
    counter[winners] += 1. / len(winners)

print(counter)
