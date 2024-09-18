def removeDuplicate(arr):
    result=[]
    for i in arr:
        if not i in result:
            result.append(i)

    return(result)

print(removeDuplicate([2, 2, 2, 2, 2]))
print(removeDuplicate([1, 2, 2, 3, 4, 4, 4, 5, 5]))