import datetime


def format_date_joined(date):
    now = datetime.datetime.now()  # today's date
    date_joined = datetime.date(2020, 2, 8)  # a specific date
    print("Joined" + date_joined.strftime("%B, %Y"))
