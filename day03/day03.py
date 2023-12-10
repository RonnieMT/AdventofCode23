with open("day02_input.txt") as f:
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    total = 0
    moves = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
    for line in f.readlines(): 
        