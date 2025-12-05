def camelcase(s):
    words_count = 1
    
    for char in s:
        uppercased_char = char.capitalize()
        if char == uppercased_char:
            words_count += 1
            
    return words_count