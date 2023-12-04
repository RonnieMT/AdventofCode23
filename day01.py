with open("day01_input.txt") as f:
    num_1 = ""
    num_2 = ""
    total = 0
    for line in f.readlines():
        
        numbers = []
        for char in line:
            if char.isdigit():
                numbers.append(char)
        num_1 = numbers[0]
        num_2 = numbers[len(numbers)-1]
        num = num_1 + num_2
        total += int(num)
    print(total)
