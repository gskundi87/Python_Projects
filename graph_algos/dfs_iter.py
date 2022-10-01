# Adj_G is an adjacency list of graph G
# All verticies contain internal structure for being visited and parent

dfs_iter(Adj_G, start):
	start.parent = None
	s = new stack()
	s.push(start)

	while len(s) is not 0:
		u = s.pop()

		if u.visited is False:
			u.visited = True

			for v in Adj_G[u]:
				v.parent = u
				s.push(v)