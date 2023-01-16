def countingValleys(steps, path):
    
    # Write your code here
    count_valleys = 0
    height = 0
    sea_level = 0
    
    for i in range(steps):
        direction = path[i]
        if direction == 'U':
            height += 1
        else:
            height -= 1
            
        if height == sea_level and direction == 'U':
            count_valleys += 1
    return count_valleys
