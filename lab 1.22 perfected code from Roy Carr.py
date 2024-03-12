age_years = int(input())
weight_pounds = int(input())
heart_bpm = int(input())
time_minutes = int(input())

calories = ((age_years * 0.2757) + (weight_pounds * 0.03295) + (heart_bpm * 1.0781) - 75.4991) * time_minutes / 8.368

print('Calories: {:.2f} calories'.format(calories))
