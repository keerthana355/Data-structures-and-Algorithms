def nextGreater(arr, size):
    for i in range(size):
        flag = False
        for j in range(i + 1, size):
            if arr[j] > arr[i]:
                print(arr[j], end=" ")
                flag = True
                break
        if not flag:
            print("-", end=" ")

# Driver Code
arr = [30, 50, 20, 15, 25]
size = len(arr)
nextGreater(arr, size)