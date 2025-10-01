from datetime import datetime

time = "05/05/2024 8:30AM"

dt = datetime.strptime(time, "%m/%d/%Y %I:%M%p")

utc = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

print(utc)
