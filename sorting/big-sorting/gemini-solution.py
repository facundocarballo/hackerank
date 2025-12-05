def bigSorting(unsorted):
    sorted_result = sorted(unsorted, key=lambda x: (len(x), x))
    
    return sorted_result