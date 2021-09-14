import numpy as np

def roll_die():
    die_values = [1,2,3,4,5,6]
    return np.random.choice(die_values)

def check_pascal_count():
    double_six = 0
    current_roll = None

    for i in range(24):
        current_roll = roll_die()
        current_roll += roll_die()
        if current_roll == 12:
            double_six += 1
            break

    return double_six

def run_simulation(trials):
    count = 0.0
    for i in range(trials):
        count += check_pascal_count()

    return count / trials

print(run_simulation(10000))
    