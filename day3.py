if __name__ == '__main__':
    def read_numbers_into_list():
        tuber_list = []
        guard_list = []
        
        with open('day3input.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                if any(char in line for char in ['^', 'v', '<', '>']):
                    parts = line.split(',')
                    x = int(parts[0])
                    y_and_dir = parts[1].strip().split(' ')
                    y = int(y_and_dir[0])
                    direction = y_and_dir[1]
                    
                    guard_list.append((x, y, direction))
                else:
                    parts = line.split(',')
                    tuber = (int(parts[0]), int(parts[1]))
                    tuber_list.append(tuber)
                    
        return tuber_list, guard_list

    
    tuber_list, guard_list = read_numbers_into_list()
    # going to assume graph is 300 by 300

    
    # We will make a safe matrix to see what areas are spotted by guards
    safe_matrix = [[True] * 300 for i in range(300)]
    count = 0
    for r in safe_matrix:
        for c in safe_matrix:
            count += 1

    for gx, gy, direction in guard_list:
        # Bounding box for 10-unit radius
        for row in range(max(0, gy - 10), min(300, gy + 11)):
            for col in range(max(0, gx - 10), min(300, gx + 11)):
                
                # don't need abs() as we will square
                dx = col - gx
                dy = row - gy
                # euclidean distance
                dist_sq = dx**2 + dy**2
                
                # only check if our euclidean distance for the cell is within 10 cells (sqroot of 100)
                if dist_sq <= 100:
                    is_visible = False
                    
                    # only mark visible in correct looking direction
                    if direction == 'v':
                        if row <= gy and abs(dx) <= abs(dy):
                            is_visible = True
                    elif direction == '^':
                        if row >= gy and abs(dx) <= abs(dy):
                            is_visible = True
                    elif direction == '>':
                        if col >= gx and abs(dy) <= abs(dx):
                            is_visible = True
                    elif direction == '<':
                        if col <= gx and abs(dy) <= abs(dx):
                            is_visible = True
                    
                    if is_visible:
                        safe_matrix[row][col] = False

    res = 0
    for tuber_x, tuber_y in tuber_list:
        if safe_matrix[tuber_y][tuber_x] == True:
            res += 1
    print(res)
