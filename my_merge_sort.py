def merge_sort(lst):
    if len(lst)> 1:
        i = len(lst)/2
        left = lst[:i]
        right = lst[i:]
        merge_sort(left)
        merge_sort(right)
        merge(lst,left,right)

def merge(lst,left,right):
    i= 0
    j= 0
    k = 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            lst[k] = left[i]
            i+=1
        else:
            lst[k] = right[j]
            j+=1
        k+=1

    lst[k:] = left[i:] + right[j:]
