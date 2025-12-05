def equalizeArray(arr):
    hash_map = {}
    
    for number in arr:
        hash_map[number] = hash_map.get(number, 0) + 1
        
    times_appear = 0
    elements_to_delete = 0
    
    for number in hash_map:
        if hash_map[number] > times_appear:
            elements_to_delete += times_appear
            times_appear = hash_map[number]
        else:
            elements_to_delete += hash_map[number]
            
    return elements_to_delete