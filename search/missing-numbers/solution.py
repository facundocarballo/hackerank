def missingNumbers(arr, brr):
    hash_map_brr = {}
    hash_map_arr = {}
    
    result = []
    
    for num in brr:
        value = hash_map_brr.get(num, 0)
        hash_map_brr[num] = value + 1
    
    for num in arr:
        value = hash_map_arr.get(num, 0)
        hash_map_arr[num] = value + 1

    for key in hash_map_brr.keys():
        try:
            if hash_map_brr[key] != hash_map_arr[key]:
                result.append(key)
        except KeyError:
            result.append(key)

    return sorted(result)

arr = [7, 2, 5, 3, 5, 3]
brr = [7, 2, 5, 4, 6, 3, 5, 3]

print(missingNumbers(arr, brr))
