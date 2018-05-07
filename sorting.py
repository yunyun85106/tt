#soritng code

#bubble sort, time O(n^2)

#Time O(n^2), Space: in space
def selection_sort(array):

	#print(len(array))
	for i in range(len(array)-1):
		cur_min = i
		for j in range(i+1, len(array)):
			if (array[j]<array[cur_min]):
				cur_min = j
		temp = array[i]
		array[i] = array[cur_min]
		array[cur_min] =  temp
	return array



#insertion is better than selection and bubble
#time O(n^2), space: in space
def insertion_sort(array):
	for i in range(len(array)):
		value = array[i]
		hole = i
		while (hole>0 and array[hole-1]>value):
			array[hole] = array[hole-1]
			hole -=1
		array[hole] = value
	return array

#merge sort
#not in place O(n), time  = theta(nlogn)
#space is  O(n)
def merge(l, r, ar):
	len_l = len(l)
	len_r = len(r)
	i = j = k = 0  # i =left index, j = right index, k = original index
	while(i<len_l and j <len_r):
		if (l[i]<=r[j]):
			ar[k] = l[i]
			i+=1
		else:
			a[k] = r[j]
			j+=1
		k+=1
	while (i<len_l):
		ar[k] = l[i]
		i+=1
		k+=1
	while (j<len_r):
		ar[k] = r[j]
		j+=1
		k+=1
	return ar

def mergesort(array):
	n = len(array)
	if (n<2):
		return 
	mid = n//2
	left = array[:mid]
	right = array[mid:]
	mergesort(left)
	mergesort(right)
	return merge(left, right,array)


#quick sort: time O(nlogn) best and average, worse O(n^2) can be avioded
# but in place
#fast and efficient in practical, not stable
def quicksort_help(ar):
	quicksort(ar, 0, len(ar)-1)
	return ar

def quicksort(ar, start, end):
	if start >= end:
		return
	pindex = partition(ar, start, end)
	quicksort(ar, start, pindex-1)
	quicksort(ar, pindex+1, end)

def partition(ar, start, end):
	pivot = ar[end]
	pindex = start
	for i in range(start,end):
		if(ar[i]<=pivot):
			ar[i], ar[pindex] = ar[pindex], ar[i]
			pindex+=1 
	ar[pindex], ar[end] = ar[end], ar[pindex]
	print(pindex, ar)
	return pindex



def main():
	my_array = [2,7,4,1,5,3,0]
	#sorted1 = selection_sort(my_array)
	#sorted2 = insertion_sort(my_array)
	#sorted3 = mergesort(my_array)
	#sorted4 = quicksort_help(my_array)
	#print(sorted1)
	#print(sorted2)
	#print(sorted3)
	#print(sorted4)
	



		



if __name__ == "__main__":
    main()

