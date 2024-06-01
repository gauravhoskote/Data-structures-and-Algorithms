class CustomHeap:
	
	# insert
	# get min and max
	# extract min max
	# update
	# build -- done


	def __init__(self, arr = None, heap_func = min):
		self.heap = []
		self.heap_func = heap_func
		
		if arr:
			self.heapify(arr)

	def show(self):
		print(self.heap)
	
	def _sift_up(self, index):
		if index != 0:
			parent = (index-1)//2
			if self.heap_func(self.heap[parent], self.heap[index]) == self.heap[index]:
				self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
				self._sift_up(parent)

	def _sift_down(self, index):
		left_index = 2 * index + 1
		right_index = 2 * index + 2
		if left_index < len(self.heap) or right_index < len(self.heap):
			if right_index < len(self.heap):
				if self.heap[left_index] == self.heap_func(self.heap[left_index], self.heap[right_index]):
					better_index = left_index
				else:
					if right_index < len(self.heap):
						better_index = right_index
					else:
						return
			else:
				better_index = left_index
			if self.heap[better_index] == self.heap_func(self.heap[better_index], self.heap[index]):
				# swap those elements
				self.heap[better_index], self.heap[index] = self.heap[index], self.heap[better_index]
				self._sift_down(better_index)


	def heapify(self, arr):
		self.heap = arr
		for i in reversed(range(len(arr))):
			print(i)
			self._sift_down(i)

	def insert(self, element):
		self.heap.append(element)
		self._sift_up(len(self.heap)-1)

	def get_top(self):
		return self.heap[0]

	def pop(self):
		# swap the elements
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		self.heap.pop()
		# the sift down the top
		self._sift_down(0)



arr = [2, 4, 8, 1, 5]
hp = CustomHeap(arr, min)
print(hp.heap)

hp.insert(-1)


print(hp.heap)


while hp.heap:
	print(hp.get_top())
	hp.pop()






