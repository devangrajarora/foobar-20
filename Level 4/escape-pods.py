def solution(entrances, exits, path):

	entrySet = set(entrances)
	exitSet = set(exits)
	n = len(path)
	adj = [[] for i in range(n)]

	# print(adj)
	for i in range(n):
		if i not in exitSet:
			for j in range(n):
				if path[i][j] != 0: 
					adj[i].append([j,path[i][j]])

	q = []
	cnt = 0
	for i in range(n):
		if i in entrySet:
			for s in adj[i]:
				# [curr node, no of bunnies, cnt]
				# ans is summation of all cnts 
				s.append(cnt)
				q.append(s)
				cnt += 1

	arr = [0]*cnt
	vis = [[False for j in range(cnt)] for i in range(n)]

	while q:

		# print(q)
		curr,bunniesTillNow,origin = q.pop(0)

		if curr in exitSet:
			if bunniesTillNow > arr[origin]:
				arr[origin] = bunniesTillNow

		vis[curr][origin] = True

		for node in adj[curr]:

			nextNode = node[0]
			nextBunnies = node[1] 
			if vis[nextNode][origin]:
				continue
			
			# vis[nextNode][origin] = True
			bunniesTransferred = min(bunniesTillNow, nextBunnies)
			q.append([node[0], bunniesTransferred, origin])

	return sum(arr)


if __name__ == '__main__':
	
	entrances = [0]
	exits = [3]
	path = [[0, 6, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5], [9, 0, 0, 0]]
	ans = solution(entrances,exits,path)
	print(ans)

	entrances = [0, 1]
	exits =  [4, 5]
	path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
	ans = solution(entrances,exits,path)
	print(ans)
