
max_str = ""
max_length = 0

min_str = ""
min_length = 0

def search_idx_right(sorted_arr, num_value, start_point):    
    sorted_arr_value = int(sorted_arr[start_point])
    
    if num_value > sorted_arr_value:
        new_start_point = start_point + int(start_point/2)
        return search_idx_right(sorted_arr, num_value, new_start_point)
    
    if num_value < sorted_arr_value:
        new_end_point = start_point - int(start_point/2)
        return search_idx_left(sorted_arr, num_value, new_end_point)
        
    return start_point

def search_idx_left(sorted_arr, num_value, end_point):
    sorted_arr_value = int(sorted_arr[end_point])
    
    if num_value > sorted_arr_value:
        new_start_point = end_point + int(end_point / 2)
        return search_idx_right(sorted_arr, num_value, new_start_point)
    
    if num_value < sorted_arr_value:
        new_end_point = int(end_point/2)
        return search_idx_left(sorted_arr, num_value, new_end_point)
    
    return end_point

def search_idx(sorted_arr, num_str):
    i = int(len(sorted_arr) / 2)
    
    num_value = int(num_str)
    sorted_arr_value = int(sorted_arr[i])
    
    if num_value > sorted_arr_value:
        return search_idx_right(sorted_arr, num_value, i+1)
        
    if num_value < sorted_arr_value:
        return search_idx_left(sorted_arr, num_value, i-1)

def get_idx_to_insert(sorted_arr, num_str):
    global max_length
    global max_str
    
    global min_length
    global min_str
    
    num_len = len(num_str)
    
    if (num_len > max_length):
        max_length = num_len
        max_str = num_str
        return len(sorted_arr)
    
    if (num_len < min_length):
        min_length = num_len
        min_str = num_str
        return 0
    
    return search_idx(sorted_arr, num_str)
    
def bigSorting(unsorted):
    sorted_arr = []
    
    for str_num in unsorted:
        idx_to_insert = get_idx_to_insert(sorted_arr, str_num)
        sorted_arr.insert(idx_to_insert, str_num)

    return sorted_arr
