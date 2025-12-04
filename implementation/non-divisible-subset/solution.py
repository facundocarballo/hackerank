def nonDivisibleSubset(k, s):
    hash_map = {}
    set_s = set(s)
    list_s = list(set_s)
    
    for i in range(k):
        hash_map[i] = []

    for i in range(len(list_s)):
        mod = list_s[i] % k
        hash_map[mod].append(list_s[i])

    aux = []
    if len(hash_map[0]) > 0:
        aux.append(1)
        
    for i in range(1, int(k/2) + 1):
        if i == k/2 and len(hash_map[i]) > 0:
            aux.append(1)
            continue
            
        first_value = len(hash_map[i])
        second_value = len(hash_map[k - i])

        if (first_value > second_value):
            aux.append(first_value)
        else:
            aux.append(second_value)
        
    result = 0
    for i in range(len(aux)):
        result += aux[i] 

    return result

input = [1, 7, 2, 4]
k = 3

result = nonDivisibleSubset(k, input)
print("Result: ", result)