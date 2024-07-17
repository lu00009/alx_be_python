import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is: {formatted_datetime}")

def calculate_future_date():
    num_days = int(input("Enter a number of days: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=num_days)
    formatted_datetime = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is: {formatted_datetime}")

display_current_datetime()
calculate_future_date()
