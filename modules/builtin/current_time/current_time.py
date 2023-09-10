from datetime import datetime

def main():
    now = datetime.now()

    current_time = now.strftime("%H:%M")

    return f"The time is {current_time}"