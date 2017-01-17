def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf) # doesn't do anything if len = 1; considered sorted
        mergeSort(righthalf) # doesn't do anything if len = 1; considered sorted
        merge(alist,lefthalf,righthalf)

def merge(alist,lefthalf,righthalf):
    i=0 # counter that looks through left half
    j=0 # counter that looks through right half
    k=0 # keeps track of of place in total sorted array
    while i < len(lefthalf) and j < len(righthalf): # compares values for subset of left and right that have same number of entries
        if lefthalf[i] < righthalf[j]:
            alist[k]=lefthalf[i]
            i=i+1
        else:
            alist[k]=righthalf[j]
            j=j+1
        k=k+1

    # for when left half or right half is exhausted
    # while i < len(lefthalf):
    #     alist[k]=lefthalf[i]
    #     i=i+1
    #     k=k+1
    # 
    # while j < len(righthalf):
    #    alist[k]=righthalf[j]
    #    j=j+1
    #    k=k+1
    alist[k:] = lefthalf[i:] + righthalf[j:]
print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
