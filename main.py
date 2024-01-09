import csv
import numpy
from collections import defaultdict

HEADER_ROWS = 5

NAME_INDEX = 1
SEX_CATEGORY_INDEX = 2
AGE_CATEGORY_INDEX = 5
WEIGHT_CATEGORY_INDEX = 7

SQUAT_FIRST_ATTEMPT_INDEX=8
SQUAT_LAST_ATTEMPT_INDEX=10

BENCH_FIRST_ATTEMPT_INDEX=11
BENCH_LAST_ATTEMPT_INDEX=13

DEADLIFT_FIRST_ATTEMPT_INDEX=14
DEADLIFT_LAST_ATTEMPT_INDEX=16

data = numpy.array(list(csv.reader(open("data.csv", "r"), delimiter=",")))[HEADER_ROWS:]

max_dict = {}

def get_max_lifts_for_row(row, start_index, end_index):
    lifts = [float(lift.replace(',', '.')) for lift in row[start_index:end_index+1] if lift]
    if not len(lifts): return 0
    return max(lifts)

def print_lifts(lifts, lift_name=""):
    for k, v in lifts.items():
        print(" ".join(k) + " " +lift_name)
        print("{:<8} {:<15} {:<20}".format('Place', 'Weight', 'Name'))
        for i in range(len(v)):
          print("{:<8} {:<15} {:<20}".format(i+1, v[i][1], v[i][0]))

        print('\n')

def find_squat(data, top_n=3):
    top_values = defaultdict(list)

    for row in data[1:]:
        sex = row[SEX_CATEGORY_INDEX]
        age = row[AGE_CATEGORY_INDEX]
        weight = row[WEIGHT_CATEGORY_INDEX]
        name = row[NAME_INDEX]

        key = (sex, age, weight)
        squat_value = get_max_lifts_for_row(row, SQUAT_FIRST_ATTEMPT_INDEX, SQUAT_LAST_ATTEMPT_INDEX)

        current_top_values = top_values[key]
        if len(current_top_values) < top_n or squat_value > min([x[1] for x in current_top_values]):
            current_top_values = top_values[key]
            current_top_values.append((name, squat_value))
            current_top_values.sort(key=lambda x: x[1], reverse=True)
            current_top_values = current_top_values[:top_n]

            top_values[key] = current_top_values

    return top_values

def find_bench(data, top_n=3):
    top_values = defaultdict(list)

    for row in data[1:]:
        sex = row[SEX_CATEGORY_INDEX]
        age = row[AGE_CATEGORY_INDEX]
        weight = row[WEIGHT_CATEGORY_INDEX]
        name = row[NAME_INDEX]

        key = (sex, age, weight)
        bench_value = get_max_lifts_for_row(row, BENCH_FIRST_ATTEMPT_INDEX, BENCH_LAST_ATTEMPT_INDEX)

        current_top_values = top_values[key]
        if len(current_top_values) < top_n or bench_value > min([x[1] for x in current_top_values]):
            current_top_values = top_values[key]
            current_top_values.append((name, bench_value))
            current_top_values.sort(key=lambda x: x[1], reverse=True)
            current_top_values = current_top_values[:top_n]

            top_values[key] = current_top_values

    return top_values

def find_deadlift(data, top_n=3):
    top_values = defaultdict(list)

    for row in data[1:]:
        sex = row[SEX_CATEGORY_INDEX]
        age = row[AGE_CATEGORY_INDEX]
        weight = row[WEIGHT_CATEGORY_INDEX]
        name = row[NAME_INDEX]

        key = (sex, age, weight)
        deadlift_value = get_max_lifts_for_row(row, DEADLIFT_FIRST_ATTEMPT_INDEX, DEADLIFT_LAST_ATTEMPT_INDEX)

        current_top_values = top_values[key]
        if len(current_top_values) < top_n or deadlift_value > min([x[1] for x in current_top_values]):
            current_top_values = top_values[key]
            current_top_values.append((name, deadlift_value))
            current_top_values.sort(key=lambda x: x[1], reverse=True)
            current_top_values = current_top_values[:top_n]

            top_values[key] = current_top_values

    return top_values

squat = find_squat(data)
bench = find_bench(data)
deadlift = find_deadlift(data)

print_lifts(deadlift, lift_name="Deadlift")