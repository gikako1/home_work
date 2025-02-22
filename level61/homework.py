#1) მანუალური ფილტრი
def manual_filter(arr, *target):
    return print([elem for elem in arr if elem not in target])
manual_filter([1,2,3,4,5],3)

#2) მანუალური სორტი
def manual_sort(arr):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted=False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return print(arr)

manual_sort([1,6,3,5,7,9,15,3])