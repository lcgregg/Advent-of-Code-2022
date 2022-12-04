import heapq


def add_to_max_heap(heap, val, size = 1):
    heapq.heappush(heap, val)
    if len(heap) > size:
        heapq.heappop(heap)
    return heap


def calorie_counter(inventory):
    '''
    return array of top 3 max_cals being carried
        inventory is a txt file where the elves write the calories of the items
        a given elf's items are separated by a blank line
    '''

    calorie_count = 0
    max_cals = []

    with open(inventory, "r") as f:
        for x in f:
            if x!='\n':
                calorie_count += float(x)
            else:
                max_cals = add_to_max_heap(max_cals, calorie_count, 3)
                calorie_count = 0
    max_cals = add_to_max_heap(max_cals, calorie_count, 3)

    return max_cals