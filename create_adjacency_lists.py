from collections import defaultdict
def addedge(d,n1,n2):
	d[n1].append(n2)
	d[n2].append(n1)

def print_adjaceny_list(n):
	d = {}
	for i in range(n):
		d[i] = []
	addedge(d,0,1)
	addedge(d,0,2)
	addedge(d,1,2)
	addedge(d,2,3)
	print(d)
print_adjaceny_list(4)