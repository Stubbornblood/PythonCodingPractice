# def bubble_sort(arr):
#     n = len(arr)
    
#     for i in range(n):
#         print(arr)
#         for j in range(0,n-i-1):
#             if arr[j]<arr[j+1]:
                
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
                
    
#     return arr           
            
        






def bubble_Sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                
    return a
                
            


my_array = [64, 34, 25, 12, 22, 11, 90]

bubble_Sort(my_array)

print("Sorted array:", my_array)