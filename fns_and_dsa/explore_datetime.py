import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f'{current_date:%d/%m/%Y %H:%M}')
display_current_datetime()
days = int(input("please enter days number"))
def calculate_future_date(days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    print(f'{future_date:%d/%m/%Y}')
calculate_future_date(days)