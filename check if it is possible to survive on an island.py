S = 10  # Number of days you are required to survive.
N = 20  # Maximum unit of food you can buy each day.
M = 30  # Unit of food required each day to survive.

x = S//7  # Number of sundays
y = S-x

total_unit_of_food_required_to_survive = S*M
if total_unit_of_food_required_to_survive // N == 0:
    number_of_days_needed_to_buy_food = total_unit_of_food_required_to_survive % N
else:
    number_of_days_needed_to_buy_food = (
        total_unit_of_food_required_to_survive // N) + 1

if number_of_days_needed_to_buy_food < y:
    print(True)
else:
    print(False)
