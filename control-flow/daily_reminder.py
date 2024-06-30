task = input("Enter your task:")
priority = input ("Priority (high/medium/low):").lower()
time_bound = input ("Is it time_bound? (yes/no):").lower()
reminder = ""
match priority:
    case "high":
        reminder = f"'{task}' is of high priority task "
    case "medium":
        reminder = f"'{task}' is of medium priority."
    case "low":
        reminder = f"'{task}' is of low priority task. "
    case _:
        reminder = f"'{task}' has an unspecified priority."
if time_bound == "yes":
    reminder += "requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    reminder += "Consider completing it when you have free time."
    print(f"Note: {reminder}")
