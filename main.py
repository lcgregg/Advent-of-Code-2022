from day1_caloriecounter import calorie_counter

if __name__ == "__main__":
    max_cals = calorie_counter("input/day1.txt")
    print(f"top 3 most calories: {max_cals} (total {sum(max_cals)})")