from day1_caloriecounter import calorie_counter

if __name__ == "__main__":
    elf_w_most_cals = calorie_counter("input/day1.txt")
    print(f"elf #{elf_w_most_cals[0]} has the most food ({elf_w_most_cals[1]}C)")