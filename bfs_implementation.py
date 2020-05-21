import queue
def add_edge(d,n1,n2):
	d[n1].append(n2)
	d[n2].append(n1)

def print_bfs(n,src):

	d = {}
	for i in range(n):
		d[i] = []

	add_edge(d,0,1)
	add_edge(d,0,2)
	add_edge(d,1,2)
	add_edge(d,1,3)
	add_edge(d,2,3)
	add_edge(d,2,4)
	add_edge(d,3,4)

	visited = [False]*n

	q = queue.Queue()
	q.put(src)
	visited[src] = True
	res = []
	while q.qsize() != 0:
		tmp = q.get()
		res.append(tmp)
		for ele in d[tmp]:
			if visited[ele] == False:
				q.put(ele)
				visited[ele] = True


	print(res)

print_bfs(5,1)