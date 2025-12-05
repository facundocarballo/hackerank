# This solution is ok for the most cases, but it's O(N^2)

max_value = 0

def get_idx_to_insert(sorted_arr, num):
    if (num > max_value):
        max_value = num
        return len(sorted_arr)
    i = 0
    
    while i < len(sorted_arr) and num > sorted_arr[i]:
        i += 1
    
    if i == len(sorted_arr):
        max_value = num
    
    return i
    
def bigSorting(unsorted):
    sorted_arr = []
    
    for str_num in unsorted:
        num = int(str_num)
        idx_to_insert = get_idx_to_insert(sorted_arr, num)
        sorted_arr.insert(idx_to_insert, num)

    
    string_arr = []
    for num in sorted_arr:
        string_arr.append(str(num))
    
    return string_arr

unsorted = [6, 3, 5, 1, 2, 4]
print(bigSorting(unsorted))