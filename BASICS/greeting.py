import time

# Get the full timestamp to print
timestamp = time.strftime('%H:%M:%S')
print(f"Current Time: {timestamp}")

# Extract just the hour as an integer ONCE and store it
current_hour = int(time.strftime('%H'))

# Logic using the 24-hour format
if current_hour < 12:
    print("Good Morning")
elif current_hour >= 12 and current_hour < 17:  # 12 PM up to 4:59 PM
    print("Good Afternoon")
else:
    print("Good Evening")