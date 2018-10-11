
# 用邻接表表示图
graph = {
	'A':['B','C'],
	'B':['A','C','D'],
	'C':['A','B','D','E'],
	'D':['B','C','E','F'],
	'E':['C','D'],
	'F':['D']
}

# 广度优先搜索
def BFS(graph,start):
	queue = []
	queue.append(start)

	seen = set()
	seen.add(start)

	while(len(queue) > 0):
		vertex = queue.pop(0)
		neighbor_nodes = graph[vertex]

		for w in neighbor_nodes:
			if w not in seen:
				queue.append(w)
				seen.add(w)
		print(vertex)

BFS(graph, 'A')