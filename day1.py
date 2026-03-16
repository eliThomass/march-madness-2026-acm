# The Muddy ArrivalThe Muddy Arrival
# On your way to ACM General, the ground vanished. After a dizzying fall through a purple void, you stick the landing face-first into a pile of very soft, very damp moss.
# 
# As you scrape the moss off your face, you find yourself surrounded by a group of large, remarkably chill rodents. "Welcome to Capybara Village," one says, balancing a lemon on its head. "You fell from the Sky-Void. Happens sometimes. If you want to get back, you'll need the Super Cannon, but it’s been lost since the Great Mango Winter."
# 
# Part One
# The village elder tells you the first step is to visit the Fruit Shop across the Great Muddy River to gather supplies. However, the bridge is washed out. To cross, you need to place stepping stones.
# 
# The capybaras give you a list of "Elevation heights" for the riverbed. To make a stable path, you need to identify "Safety Peaks". A Safety Peak is the first riverbed coordinate to the right of your current position that is strictly taller than the one you are standing on. If there is no taller coordinate ahead, you’ll just have to leap into the mud (represented by a -1).
# 
# You are given a list of riverbed heights. For each position, find the height of the next taller stone to its right.
# 
# For example, if the riverbed heights are:
# 
# 4
# 2
# 5
# 3
# - At 4, the next taller stone is 5.
# - At 2, the next taller stone is 5.
# - At 5, there is nothing taller to the right, so -1.
# - At 3, there is nothing taller to the right, so -1.
# Result: [5, 5, -1, -1] The sum of these heights is 5 + 5 = 10. So, the answer for this example would be 10.
# 
# Given the list of riverbed heights, what is the sum of all the "Safety Peak" heights? (Exclude the -1s from your sum).


def read_numbers_into_list():
    numbers_list = []
    with open('day1input.txt', 'r') as file:
        for line in file:
            number = int(line.strip())
            numbers_list.append(number)
    return numbers_list

if __name__ == "__main__":

    # PART 1 OF PROBLEM

    stones = read_numbers_into_list()

    res = 0
    
    for i in range(len(stones)):
        for j in range(i, len(stones)):
            if stones[j] > stones[i]:
                res += stones[j]
                break

    print(res)

    # PART 2 OF PROBLEM

    spans = 0

    for i in range(len(stones)):
        span = 1
        curr_h = stones[i]
        span_i = i - 1
        while span_i >= 0:
            span_h = stones[span_i]
            if span_h > curr_h:
                break
            span += 1
            span_i -= 1
        spans += span

    print(spans)
