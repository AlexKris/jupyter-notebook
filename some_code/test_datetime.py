from datetime import datetime, timedelta

start_date_str = '2022-01-01'
end_date_str = '2022-12-31'

start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

date_range = end_date - start_date

for n in range(date_range.days + 1):
    date = start_date + timedelta(n)
    print(date.strftime('%Y-%m-%d'))