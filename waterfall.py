from collections import deque

def waterfall(array, source):
	position = [0, source, 100]
	queue = deque()
	queue.append(position)
	answer = [0 for i in range(len(array[0]))]
	while queue:
		x, y, quantity = queue.popleft()
		if x + 1 == len(array):
			answer[y] += quantity

		if x + 1 < len(array):
			if array[x+1][y] == 0:
				queue.append([x+1,y,quantity])

			elif array[x+1][y] == 1:
				# handle left half
				i = 1
				while y-i >= 0 and array[x][y-i] == 0 and array[x+1][y-i] == 1:
					i += 1

				if y-i >= 0 and array[x][y-i] == 0 and array[x+1][y-i]==0:
					queue.append([x+1, y-i, quantity/2])


				# handle right half
				i = 1
				while y+i < len(array[0]) and array[x][y+i] == 0 and array[x+1][y+i] == 1:
					i += 1

				if y+i < len(array[0]) and array[x][y+i] == 0 and array[x+1][y+i] == 0:
					queue.append([x+1, y+i, quantity/2])

	return answer
