obstacles_map = {}

def fill_obstacles(obstacles):
    for obstacle in obstacles:
        o_row = obstacle[0]
        o_column = obstacle[1]
        
        coordenate = f"{o_row}, {o_column}"
        
        obstacles_map[coordenate] = True
        

def is_an_obstacle(row, column) -> bool:
    coordenates = f"{row}, {column}"
    return obstacles_map.get(coordenates, False)

def queensAttack(n, k, r_q, c_q, obstacles):
    fill_obstacles(obstacles)
    
    squares_to_attack = 0
    
    # How many squares can attack - UP
    next_row = r_q + 1
    while next_row <= n:
        if is_an_obstacle(next_row, c_q):
            break
        squares_to_attack += 1
        next_row += 1
        
    # How many squares can attack - DOWN
    next_row = r_q - 1
    while next_row > 0:
        if is_an_obstacle(next_row, c_q):
            break
        squares_to_attack += 1
        next_row -= 1
        
    # How many squares can attack - LEFT
    next_column = c_q - 1
    while next_column > 0:
        if is_an_obstacle(r_q, next_column):
            break
        squares_to_attack += 1
        next_column -= 1
        
    # How many squares can attack - RIGHT
    next_column = c_q + 1
    while next_column <= n:
        if is_an_obstacle(r_q, next_column):
            break
        squares_to_attack += 1
        next_column += 1

    # Diagonal UP-LEFT
    next_row = r_q + 1
    next_column = c_q - 1
    while next_row <= n and next_column > 0:
        if is_an_obstacle(next_row, next_column):
            break
        squares_to_attack += 1
        next_column -= 1
        next_row += 1
        
    # Diagonal DOWN-LEFT
    next_row = r_q - 1
    next_column = c_q - 1
    while next_row > 0 and next_column > 0:
        if is_an_obstacle(next_row, next_column):
            break
        squares_to_attack += 1
        next_column -= 1
        next_row -= 1
    
    # Diagonal DOWN-RIGHT
    next_row = r_q - 1
    next_column = c_q + 1
    while next_row > 0 and next_column <= n:
        if is_an_obstacle(next_row, next_column):
            break
        squares_to_attack += 1
        next_row -= 1
        next_column += 1
        
    # Diagonal UP-RIGHT
    next_row = r_q + 1
    next_column = c_q + 1
    while next_row <= n and next_column <= n:
        if is_an_obstacle(next_row, next_column):
            break
        squares_to_attack += 1
        next_row += 1
        next_column += 1
            
    return squares_to_attack
n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [[5, 5], [4, 2], [2, 3]]

result = queensAttack(n, k, r_q, c_q, obstacles)

print("Result: ", result)

if (result == 10):
    print("Test 1 passed")
else:
    print("Test 1 failed")