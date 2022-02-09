# Python implemenatation of stack and queue
# DSA day 1

list1 = [1, 2, 3, 4, 5]

def push(listx, n):
	listx.append(n)
	print("Added element")
	print(listx)

def pop(listx, n):
	listx.pop()
	print("Popped Element")
	print(listx)

push(list1, 4)

pop(list1, 3)

def enqueue(listx, n):
	listx.insert(0, n)
	print("Element enqueued")
	print(listx)

def dequeue(listx, n):
	listx.pop()
	print("Element dequeued")
	print(listx)

enqueue(list1, 10)

dequeue(list1,10) 