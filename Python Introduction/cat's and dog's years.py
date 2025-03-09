def calculate_pet_years(human_years):
    if human_years == 1:
        return [human_years, 15, 15]
    elif human_years == 2:
        return [human_years, 24, 24]
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
        return [human_years, cat_years, dog_years]

# Testing the function
print(calculate_pet_years(10))  # Output: [10, 56, 64]
print(calculate_pet_years(1))   # Output: [1, 15, 15]
print(calculate_pet_years(2))   # Output: [2, 24, 24]
