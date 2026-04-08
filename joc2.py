# Number of nodes
n = int(input())

# Read graph
graph = {}
for _ in range(n):
    data = input().split()
    node = int(data[0])
    neighbors = list(map(int, data[1:]))
    graph[node] = neighbors

# Read scores
scores = {}
for _ in range(n):
    node, val = input().split()
    scores[int(node)] = float(val)

# Total before
total_before = sum(scores.values())

# Initialize new scores
new_scores = {node: 0 for node in graph}

# Distribute influence
for node in graph:
    if len(graph[node]) == 0:
        new_scores[node] += scores[node]
    else:
        share = scores[node] / len(graph[node])
        for nei in graph[node]:
            new_scores[nei] += share

# Total after
total_after = sum(new_scores.values())

# Compare
print(total_before == total_after)