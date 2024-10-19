#selection sort

def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(n+1,n):
            if arr[j]< arr[min]:
                j=min
        arr[i],arr[min]=arr[min],arr[i]    
def buuble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for  j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if(swapped==False):
            break
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
            

def print_array(arr):
    for val in arr:
        print(val ,end=" ")
    print()   
if __name__=="__main__":
    arr=[40,20,5,4,]
    print_array(arr)
    buuble_sort(arr)
   
    print_array(arr)
    selection_sort(arr)
    print_array(arr)
    insertionSort(arr)
    print(arr)
  
