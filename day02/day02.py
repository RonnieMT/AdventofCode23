with open("day02_input.txt") as f:
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    total = 0
    for line in f.readlines(): 
        game = line.split(":")
        cube_sets = game[1].split(";")
        red_num = 0
        green_num = 0
        blue_num = 0
        fail = False
        for cube_set in cube_sets:
            cubes = cube_set.split(",")
            for cube in cubes:
                num_of_cubes = cube.split(" ")
                if cube.__contains__("red"):
                    #print(cube)  
                    #red_num += int(num_of_cubes[1])
                    red_num = max(red_num,int(num_of_cubes[1]))
                if cube.__contains__("blue"):
                    #print(cube)  
                    #blue_num += int(num_of_cubes[1])
                    blue_num = max(blue_num,int(num_of_cubes[1]))
                if cube.__contains__("green"):
                    #print(cube)
                    #green_num += int(num_of_cubes[1])
                    green_num = max(green_num, int(num_of_cubes[1]))
                #print("Red num: ", red_num, "Green num: ", green_num, "Blue num: ", blue_num)
        #         if red_num > red_limit or green_num > green_limit or blue_num > blue_limit:
        #             fail = True
        # if fail:
        #     continue
        # num = game[0].split(" ")
        # total += int(num[1])
        total += red_num * green_num * blue_num
    print(total)
        
        
        