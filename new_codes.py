import numpy as np
from random import choices

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

Nd = 2  # This is the number of topic to have a decision about
Np = 4  # This is the number of parties
Nv = 5  # This is the number of voters

dd = 2 ** Nd  # Distinct decision vectors
print("dd", dd)
ovl_mat = np.zeros((dd, dd), dtype=int)
dec_arr = np.zeros((dd, Nd), dtype=int)  # Decision array has all the dd's
prob = np.ones(dd)  # Probability measure over the opinions
prob /= np.sum(prob)
voter_vec = choices(np.arange(0, dd), prob, k=Nv)
print("VV", voter_vec)
## voter_vec : The choices() method returns a list with k  randomly selected elements from the specified sequence.
## so from a space of distinct decision vectors voter_vec is randomly assigned possible decision vector to each voter

for i in range(dd):
    dec_arr[i] = np.array(list(np.binary_repr(i, width=Nd)), dtype=int)

print("dec", dec_arr)

ovl_mat = np.zeros((dd, dd), dtype=int)

for i in range(dd):
    for j in range(dd):
        ovl_mat[i, j] = np.count_nonzero(dec_arr[i] == dec_arr[j])


## Given Np parties find the one that wins according to representative democ.

def winner_rep(x, voter_vec):
    # print("voter", voter_vec)
    comp = ovl_mat[x]  # The fighting parties
    counter = np.zeros(len(x))

    for i in range(Nv):
        listy = comp[:, voter_vec[i]]
        winner = np.argwhere(listy == np.amax(listy)).flatten()
        counter[winner] += 1. / len(winner)

    return counter


def representative_democracy_voter(Np):
    representatives = np.zeros(Np)
    new_arrays = np.array_split(voter_vec, Np, axis=0)
    for a in range(len(new_arrays)):
        representatives[a] = direct_democracy_1(new_arrays[a])[0]
    print("rep", representatives)
    representatives = np.array(representatives, dtype=int)

    winner = winner_rep(representatives, voter_vec)
    print("winner", winner)


def representative_democracy_policy(Np):
    representatives = np.zeros(Np)
    new_arrays = np.array_split(voter_vec, Np, axis=0)
    for a in range(len(new_arrays)):
        representatives[a] = direct_democracy_1(new_arrays[a])[0]
    print("rep", representatives)
    representatives = np.array(representatives, dtype=int)

    winner = winner_rep(representatives, voter_vec)
    print("winner", winner)


### What follows now are different models of chosing the best policy using direct democracy
## direct_democracy_1 gives most famous policy even if it doesnot belong in voting population

def direct_democracy_1(voter_vector):
    total = np.zeros(dd)
    best_policies = []
    freq = np.zeros(dd)
    for a in range(dd):
        print("a", a)
        print("voter", voter_vector)
        freq[a] = np.count_nonzero(voter_vector == a)
        print("freq", freq[a])
    # voter vector has the form as an example [0 2 1 3] for let us say 4 distinct policies i.e in binary reprn
    # [ 0 0]  [ 1 0] [0 1]  [ 1 1] , freq[a] checks freq of 0 in voter vector [0 2 1 3] and so on
    for a in range(dd):
        for b in range(dd):
            ovl_mat[a, b] = np.count_nonzero(dec_arr[a] == dec_arr[b])
    max_value = np.dot(ovl_mat[0, :], freq)
    for c in range(dd):
        total[c] = np.dot(ovl_mat[c, :], freq)
        if total[c] >= max_value:
            max_value = total[c]

    for d in range(dd):
        if total[d] == max_value:
            best_policies.append(d)
    return best_policies


## direct_democracy_2 gives most famous policy only if it belongs in voting population

def direct_democracy_2(voter_vector):
    best_policies = []
    voter_policies = []
    freq = np.zeros(dd)
    for a in range(dd):
        freq[a] = np.count_nonzero(voter_vector == a)
        if freq[a] != 0.0:
            voter_policies.append(a)
    dd_new = len(voter_policies)
    p = np.where(freq != 0)
    freq_new = freq[p]
    total = np.zeros(dd_new)
    dec_arr_new = np.zeros((dd_new, Nd), dtype=int)
    for i in range(dd_new):
        dec_arr_new[i] = np.array(list(np.binary_repr(voter_policies[i], width=Nd)), dtype=int)

    for a in range(dd_new):
        for b in range(dd_new):
            ovl_mat[a, b] = np.count_nonzero(dec_arr_new[a] == dec_arr_new[b])
    max_value = np.dot(ovl_mat[0, :], freq_new)
    for c in voter_policies:
        total[c] = np.dot(ovl_mat[c, :], freq_new)
        if total[c] >= max_value:
            max_value = total[c]
    for d in range(dd_new):
        if total[d] == max_value:
            best_policies.append(d)
    return best_policies


voter_vector = np.array(voter_vec)
direct_democracy_2(voter_vector)
# representative_democracy_voter(Np)
