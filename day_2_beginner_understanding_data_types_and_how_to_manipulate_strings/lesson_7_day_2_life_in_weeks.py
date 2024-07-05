age = input()
age_total = 90 
age_rest = age_total - int(age)

weeks_left = ((4680 * age_rest) / age_total)

print(f"You have {int(weeks_left)} left.")