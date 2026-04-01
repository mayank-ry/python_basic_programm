import networkx as nx
import numpy as np
G=nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes())
spll = []
for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print(f'Shortest Path B/w {u} & {v} Is : ',l)
            spll.append(l)
min_spl = min(spll)
max_spl = max(spll)
print("Minimum : ",min_spl)
print("Maximum : ",max_spl)
avg_spl = np.average(spll)
print("Average : ",avg_spl)
