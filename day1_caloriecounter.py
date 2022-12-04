def calorie_counter(inventory):
    '''
    return array of [elf_index, total_calories_being_carried]
        inventory is a txt file where the elves write the calories of the items
        a given elf's items are separated by a blank line
        elf_index starts at 0
        if 2 elves have the same # calories, the first elf index will be returned
    '''
    calorie_count = 0
    total_cals = []

    f = open(inventory, "r")
    for x in f:
        if x!='\n':
            calorie_count += float(x)
        else:
            total_cals.append(calorie_count)
            calorie_count = 0

    total_cals.append(calorie_count)
    f.close()

    return [total_cals.index(max(total_cals)), max(total_cals)]