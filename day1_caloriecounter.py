import heapq

def calorie_counter(inventory):
    '''
    return array of top 3 max_cals being carried
        inventory is a txt file where the elves write the calories of the items
        a given elf's items are separated by a blank line
    '''
    calorie_count = 0
    max_cals = []

    f = open(inventory, "r")
    for x in f:
        if x!='\n':
            calorie_count += float(x)
        else:
            heapq.heappush(max_cals, calorie_count)
            calorie_count = 0
            if len(max_cals) > 3:
                heapq.heappop(max_cals)
    f.close()

    return max_cals