from datetime import datetime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def main():
    current_date = datetime.now()

    return f'It is {weekdays[current_date.weekday()]}, {months[current_date.month]} {current_date.day}, {current_date.year}.'