arr = [22,27,16,2,18,6]
def insertion_sort(arr):
    k=0
    while k<len(arr)-1:
        print(arr)
        m=arr[k]
        index=k
        for i in range(k,len(arr)):
            if arr[i]<m:
                m=arr[i]
                index=i
        arr[k],arr[index]=m,arr[k]
        k+=1
    return arr

print(insertion_sort(arr))
