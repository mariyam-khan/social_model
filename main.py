import numpy as np
from itertools import combinations

Nd = 4  # This is the number of topic/policies to have a decision about
Np = 4  # This is the number of parties
Nv = 100  # This is the number of voters

dd = 2 ** Nd  # Distinct decision vectors

dec_arr = np.zeros((dd, Nd), dtype=int)  # Decion array has all the dd's

for i in range(dd):
    dec_arr[i] = np.array(list(np.binary_repr(i, width=Nd)), dtype=int)

# print (dec_arr)

## Now we make the overlap matrix

ovl_mat = np.zeros((dd, dd), dtype=int)

for i in range(dd):
    for j in range(dd):
        ovl_mat[i, j] = np.count_nonzero(dec_arr[i] == dec_arr[j])


# print (ovl_mat)


## Given Np parties find the one that wins according to representative democ.

def winner_uniform(x):
    comp = ovl_mat[x]  # The fighting parties

    counter = np.zeros(len(x))

    for i in range(dd):
        listy = comp[:, i]
        winner = np.argwhere(listy == np.amax(listy)).flatten()

        counter[winner] += 1. / len(winner)

    return counter


## Choice of Np parties has to be made. Let us go for all possible choice of Np parties

arr = np.arange(0, dd)

all_combis = np.array(list(combinations(arr, Np)), dtype=int)

counter = np.zeros(dd)
for i in range(all_combis.shape[0]):
    parties = all_combis[i]
    print((winner_uniform(parties)))
    counter[parties] += (winner_uniform(parties))

print(counter)









