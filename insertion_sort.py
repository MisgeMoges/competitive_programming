def insertionSort1(n, arr):
    # Write your code here
    # for i in range((n-1),0,-1):
    #     if arr[i] < arr[i-1]:
    #         tmp = arr[i]
    #         arr[i] = arr[i-1]
    #         print(*arr)
    #         arr[i-1] = tmp
    # print(*arr)  
    
    for i in range(1, n):
        key = arr[i]
        
        j = i - 1
        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            print(*arr)
        arr[j+1] = key
    print(*arr)
