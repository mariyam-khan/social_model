import numpy as np
from random import choices

Nd = 3  # This is the number of topic to have a decision about
Np = 4  # This is the number of parties
Nv = 10000  # This is the number of voters

dd = 2 ** Nd  # Distinct decision vectors
ovl_mat = np.zeros((dd, dd), dtype=int)
dec_arr = np.zeros((dd, Nd), dtype=int)  # Decision array has all the dd's
prob = np.ones(dd)  # Probability measure over the opinions
prob /= np.sum(prob)
voter_vec = choices(np.arange(0, dd), prob, k=Nv)

for i in range(dd):
    dec_arr[i] = np.array(list(np.binary_repr(i, width=Nd)), dtype=int)

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


# parties = np.array([0, 1, 6], dtype=int)

# print(winner_rep(parties, voter_vec))


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
    for c in range(dd):
        total[c] = np.dot(ovl_mat[c, :], freq)
        if total[c] >= max_value:
            max_value = total[c]

    for d in range(dd):
        if total[d] == max_value:
            best_policies.append(d)
    # print("best", best_policies)
    return best_policies


direct_democracy(voter_vec)


def representative_democracy(Np):
    representatives = np.zeros(Np)
    new_arrays = np.array_split(voter_vec, Np, axis=0)
    for a in range(len(new_arrays)):
        # print("dd", direct_democracy(new_arrays[a]))
        representatives[a] = direct_democracy(new_arrays[a])[0]
    print("rep", representatives)
    representatives = np.array(representatives, dtype=int)

    winner = winner_rep(representatives, voter_vec)
    print("winner", winner)


representative_democracy(Np)
