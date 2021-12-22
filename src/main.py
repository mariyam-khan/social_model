import numpy as np
from itertools import combinations

Nd = 2  # This is the number of topic/policies to have a decision about
Np = 3  # This is the number of parties
Nv = 10  # This is the number of voters

dd = 2 ** Nd  # Distinct decision vectors

dec_arr = np.zeros((dd, Nd), dtype=int)  # Decion array has all the dd's

for i in range(dd):
    dec_arr[i] = np.array(list(np.binary_repr(i, width=Nd)), dtype=int)

## this is a matrix whose one element would be 0/1 depending on if yes/no to the policy

## Now we make the overlap matrix

ovl_mat = np.zeros((dd, dd), dtype=int)

for i in range(dd):
    for j in range(dd):
        ovl_mat[i, j] = np.count_nonzero(dec_arr[i] == dec_arr[j])

## np.count_nonzero Counts the number of non-zero values in the array , so basically
### we loop over all rows of the decision array for and see how much overlap it has with
### other possible configs, eg [ 0 0 0 1 ] is one row of dec array i.e no to 1st, 2nd and 3rd
### policy and yes to 4th ,    [ 0 1 0 1] is another possible row of dec array and
## overlap matrix"s one elements would be 3 as 3 values are same in the two rows

print("over", ovl_mat)


## Given Np parties find the one that wins according to representative democ.

def winner_uniform(x):
    comp = ovl_mat[x]  # The fighting parties

    counter = np.zeros(len(x))

    for i in range(dd):
        print("comp", comp[:, i])
        listy = comp[:, i]
        winner = np.argwhere(listy == np.amax(listy)).flatten()

        counter[winner] += 1. / len(winner)

    return counter


## Choice of Np parties has to be made. Let us go for all possible choice of Np parties

arr = np.arange(0, dd)

all_combis = np.array(list(combinations(arr, Np)), dtype=int)
### all_combis has vectors of size np and each vecotor is a distinct possible set represtatives
## ex [ 1 0 3 ] means repr with policy no 1 , 0 and 3 where 1 is [ 001]

counter = np.zeros(dd)
for i in range(all_combis.shape[0]):
    parties = all_combis[i]
    print("party", parties)
    counter[parties] += (winner_uniform(parties))

print(counter)


## TODO
# 1. Write a code for direct democracy.
# 2. Write a code for direct and representative together i.e
# Choose representatives using direct democracy and the choose best.
# direct democracy - case where per policy most famous policy vector
# direct democracy most famous policies and then policy vector
# direct dem - best policy within voter policies
# direct dem - best policy within policy vector even if it is not in the population

