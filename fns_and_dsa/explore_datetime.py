from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is: {formatted_datetime}")
num_days = int(input("Enter a number of days: "))
def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=num_days)
    formatted_datetime = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is: {formatted_datetime}")
def main():
    display_current_datetime()
    calculate_future_date()
if __name__ == "__main__":
    main()
