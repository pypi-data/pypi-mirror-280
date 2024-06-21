import datetime

def greet():
    now = datetime.datetime.now()
    current_hour = now.hour
    
    time_msg = 'Hello ~'
    if 5 <= current_hour < 11:
        time_msg = "Good morning!"
    elif 11 <= current_hour < 13:
        time_msg = "Good noon!"
    elif 13 <= current_hour < 18:
        time_msg = "Good afternoon!"
    elif 18 <= current_hour < 21:
        time_msg = "Good evening!"
    else:
        time_msg = "Good night!"

    return '\n'.join(
        [
            "", 
            f"{time_msg} I'm hanryi.", 
            "An independent developer in HZAU. ", 
            ""
        ]
    )
