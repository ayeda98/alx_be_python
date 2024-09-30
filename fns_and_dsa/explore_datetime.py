from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.now()
    return '{current_date:%Y-%m-%d %H:%M:%S}'

days = int(input("please enter days number"))
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return f'{future_date:%Y-%m-%d}'
