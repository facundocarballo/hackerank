def repeatedString(s, n):
    a_count = s.count('a')
    complete_word_in_n = int(n / len(s))
    mod_of_the_rest_word = n % len(s)
    a_count_in_mod = s[:mod_of_the_rest_word].count('a')
    
    return a_count * complete_word_in_n + a_count_in_mod