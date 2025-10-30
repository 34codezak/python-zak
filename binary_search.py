def binary_search(arr, target):
	left, rigth = 0, len(arr) - 1
	while left <= right:
		mid = left + (right -left) // 2
		if mid == target:
			return mid
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1 # Not found
