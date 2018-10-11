
# 用邻接表表示图
graph = {
	'A':['B','C'],
	'B':['A','C','D'],
	'C':['A','B','D','E'],
	'D':['B','C','E','F'],
	'E':['C','D'],
	'F':['D']
}

# 深度优先搜索
def DFS(graph,start):
	stack = []
	stack.append(start)

	seen = set()
	seen.add(start)

	while(len(stack) > 0):
		vertex = stack.pop()
		neighbor_nodes = graph[vertex]

		for w in neighbor_nodes:
			if w not in seen:
				stack.append(w)
				seen.add(w)
		print(vertex)

DFS(graph, 'E')