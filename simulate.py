import pandas as pd
import numpy as np
import os
from collections import Counter

# ==============================================================================

DataFrame1 = pd.read_csv('STARNET.eQTLs.MatrixEQTL.Blood.cis.tbl.fdr-0.05', delimiter="\t")  # Read data from file
DataFrame2 = pd.read_csv('SNP_ref.tsv', delimiter="\t")  # Read data from file
DataFrame1["effect_allele"] = ""
DataFrame1["other_allele"] = ""


selected_columns = DataFrame2['marker_id']
new_df = selected_columns.copy()
selected_columns1 = DataFrame2['a2']
new_df1 = selected_columns1.copy()
selected_columns2 = DataFrame2['a1']
new_df2 = selected_columns2.copy()
o = DataFrame1['SNP'].values
for i in range(len(DataFrame1['SNP'].values)):
    value = o[i]
    idx = DataFrame2[DataFrame2['marker_id'] == value].index.values
    # idx2 = DataFrame1[DataFrame1['SNP'] == value].index.values
    # DataFrame1.loc[idx2, 'effect_allele'] = new_df1[idx].values
    # DataFrame1.loc[idx2, 'other_allele'] = new_df2[idx].values
    DataFrame1.loc[i, 'effect_allele'] = new_df1[idx].values
    DataFrame1.loc[i, 'other_allele'] = new_df2[idx].values

DataFrame1.to_csv("Data1.csv", index=False)