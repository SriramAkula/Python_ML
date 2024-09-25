def occurrences(list):
    occurrence = {}
    
    for i in list:
        if i in occurrence:
            occurrence[i] += 1
        else:
            occurrence[i] = 1
    
    return occurrence

list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 4]
result = occurrences(list)
print(result)
