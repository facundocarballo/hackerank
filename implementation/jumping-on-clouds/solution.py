def jumpingOnClouds(c):
    i = 0
    jumps = 0
    
    while i < len(c) - 1:
        if (i+2 < len(c) and c[i+2] == 0):
            i += 2
            jumps += 1
            continue
        i+=1
        jumps += 1    
    
    return jumps