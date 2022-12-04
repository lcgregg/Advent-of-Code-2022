import heapq

def calorie_counter(inventory):
    '''
    return max_cals being carried
        inventory is a txt file where the elves write the calories of the items
        a given elf's items are separated by a blank line\
    '''
    calorie_count = 0
    max_cals = 0

    f = open(inventory, "r")
    for x in f:
        if x!='\n':
            calorie_count += float(x)
        else:
            max_cals = max(max_cals, calorie_count)
            calorie_count = 0
    f.close()

    return max_cals