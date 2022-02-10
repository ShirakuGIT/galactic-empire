# Python implemenatation of stack and queue
# DSA day 1

list1 = [21, 42, 43, 12, 31, 27, 18]

def push(listx, n):
	listx.append(n)
	print("Added element")
	print(listx)

def pop(listx, n):
	listx.pop()
	print("Popped Element")
	print(listx)



def enqueue(listx, n):
	listx.insert(0, n)
	print("Element enqueued")
	print(listx)

def dequeue(listx, n):
	listx.pop()
	print("Element dequeued")
	print(listx)


# Binary Search implementation in Python

# The idea is to compare the target element to the
# middle element, if it is higher or lower, split
# into sub-array depending on whether its higher
# or lower, then compare again with the middle 
# element of the sub-array with the target, and 
# repeat this continuously over and over again, 
# until you reach the final target element.
# This is assuming you have a sorted list and no
# duplicate elements \(0o0)/

print(list1)

def binsearch(listx, target, high, low=0):
	if high >= low:

		middle = high+low//2

		if listx[middle] == target:
			return middle

		elif listx[middle] > target:
			return binsearch(listx, target, middle-1, low)

		elif listx[middle] < target:
			return binsearch(listx, target, high-1, middle+1)

list1 = sorted(list1)

print(list1)

print(binsearch(list1, 18, len(list1)-1))




























