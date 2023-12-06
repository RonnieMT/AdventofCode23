with open("day01_input.txt") as f:
    # part 1 
    # total = 0
    # debug = 0
    # for line in f.readlines(): 
    #     first_num = ""
    #     last_num = ""
    #     for char in line:
    #         if char.isdigit():
    #             last_num = char
    #             if first_num == "":
    #                 first_num = char
    #     if first_num == '':
    #         continue
    #     total += int(first_num + last_num)
        
    #     # if debug < 10:
    #     #     debug += 1
    #     #     print("line: " + line)
    #     #     print("first_num: " + first_num)
    #     #     print("last_num: " + last_num)
    #     #     print("total: " + str(total))
    #     #     print("")
    #     # print("line: " + line)
    # print(total)
    
    
    #part 2 
    total = 0
    debug = 0
    dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
            "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for line in f.readlines(): 
        first_num = ""
        last_num = ""
        curr_string = ""
        num = ""
        for char in line:
            if char.isdigit():
                num = char
                # print(num)
            else:
                curr_string += char
                for key in dict:
                    if curr_string.endswith(key):
                        num = dict[key]
            if not num == "":
                # print(num)
                last_num = num
                if first_num == "":
                    first_num = num    
        if first_num == "":
            continue
        
        total += int(first_num + last_num)
        
        debug += 1
        if debug > 990:
            print("line: " + line)
            print("first_num: " + first_num)
            print("last_num: " + last_num)
            print("total: " + str(total))
            print("")
            
    print(total)
        
