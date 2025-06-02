# from ogb.nodeproppred import NodePropPredDataset
# from ogb.linkproppred import LinkPropPredDataset
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import math
import sys

#num_nodes = sys.argv[1] #actual width
csr_name=sys.argv[1]
N = int(sys.argv[2]) #heatmap width
d_name = sys.argv[3]

#READ DATASET (1: EDGE LIST)
'''
d_name = "../projects/datasets/soc-LiveJournal1.txt"
txt_file = open(d_name)
u, v = [], []
for pair in txt_file:
  if '#' in pair: continue
  uv = pair.split()
  u.append(uv[0])
  v.append(uv[1])
'''

#READ DATASET (2: CSR)

#csr_name = "../GNNSim_/CSR_preprocessed.txt"
el_file = open(csr_name)

lines = el_file.readlines()
u,v = [],[]

print("Start")
for i in range(0, len(lines)):
	s, d = lines[i].split()
	u.append(int(s))
	v.append(int(d))


#DRAW HEATMAP
src, tgt = u,v
print(len(src), max(src))
print(len(tgt), max(tgt))

adj_mat = np.zeros((N, N))
blk = math.ceil(max(tgt) / N)
for i, s in enumerate(src):
  u, v = s // blk, tgt[i] // blk
  if(u >= N or v >= N):
    continue
  adj_mat[u][v] += 1
#adj_mat[v][u] += 1

df_adj_mat = pd.DataFrame(adj_mat)
ax = sns.heatmap(df_adj_mat,
                 cmap="Blues",
				 xticklabels=False,
				 yticklabels=False,
				 vmax=1000,
# vmax=80000,
#vmin=20000
				 )
ax.set_title(d_name+"("+str(N)+"X"+str(N)+")")
plt.savefig(d_name + ".png")