# Adj_G is an adjacency list of graph G
# All verticies contain internal structure for being visited and parent

dfs_rec(Adj_G, u):
	u.visited = True
	for v in Adj_G[u]:
		if v.visited is False:
			v.parent = u
			dfs_rec(Adj_G, v)