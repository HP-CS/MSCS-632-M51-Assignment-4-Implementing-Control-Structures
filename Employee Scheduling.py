import random
import pandas as pd

shifts = ["Morning", "Afternoon", "Evening"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

employees = {
    "Alice": ["Morning", "Afternoon"],
    "Bob": ["Evening", "Morning"],
    "Charlie": ["Afternoon", "Evening"],
    "David": ["Morning", "Evening"],
    "Eve": ["Afternoon", "Morning"],
    "Frank": ["Evening", "Afternoon"],
    "Grace": ["Morning", "Afternoon"],
    "Hank": ["Afternoon", "Evening"],
    "Ivy": ["Morning", "Evening"],
    "Jack": ["Evening", "Morning"]
}

schedule = {day: {shift: [] for shift in shifts} for day in days}
employee_work_days = {emp: 0 for emp in employees}  # Track assigned shifts

for day in days:
    for shift in shifts:
        available_employees = [emp for emp in employees if shift in employees[emp] and employee_work_days[emp] < 5]
        
        if len(available_employees) >= 2:
            assigned_employees = random.sample(available_employees, 2)
        else:
            assigned_employees = available_employees[:]
            remaining_needed = 2 - len(assigned_employees)
            extra_candidates = [emp for emp in employees if employee_work_days[emp] < 5 and emp not in assigned_employees]
            assigned_employees += random.sample(extra_candidates, min(remaining_needed, len(extra_candidates)))
        
        for emp in assigned_employees:
            if employee_work_days[emp] < 5:
                schedule[day][shift].append(emp)
                employee_work_days[emp] += 1

schedule_df = pd.DataFrame([{**{"Day": day}, **{shift: ", ".join(schedule[day][shift]) for shift in shifts}} for day in days])

schedule_df.to_csv("employee_schedule.csv", index=False)

print(schedule_df)
