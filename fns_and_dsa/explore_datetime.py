from datetime import datetime
from datetime import timedelta
from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    return '{current_date:%Y-%m-%d %H:%M:%S}'

days = int(input("Enter the number of days to add to the current date:"))
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime()
