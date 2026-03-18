from collections import deque

if __name__ == '__main__':
    def read_numbers_into_list():
        numbers_list = []
        with open('day2input.txt', 'r') as file:
            for line in file:
                number = int(line.strip())
                numbers_list.append(number)
        return numbers_list

    
    res = 0
    sugar = read_numbers_into_list()
    
    print(len(sugar))
    windows = []

    for i in range(0, len(sugar), 50):
        print(sugar[i])
        windows.append(max(sugar[i : i+50]))

    for i in range(1, len(windows)):
        if windows[i] - windows[i - 1] >= 10:
            res += 1


    # PART 2

    
    buffer = deque()
    cap = 100

    for s in sugar: 
        if len(buffer) == cap:
            buffer.popleft() 
        while buffer and buffer[-1] < s:
            buffer.pop() 

        buffer.append(s)

    first = buffer[0]
    mid = buffer[len(buffer) // 2]
    last = buffer[-1]

    ignition = f"{first}{mid}{last}" 

    print(ignition)
