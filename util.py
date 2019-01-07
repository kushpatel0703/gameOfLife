def printArray(arr):
    for i in range(len(arr)):
        innerString = ""
        for j in range(len(arr)):
            if arr[i][j] == 1:
                innerString += "@ "
            else:
                innerString += "X "
        print(innerString)

    print("--------------")
