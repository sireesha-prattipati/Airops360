import csv
import random
from datetime import datetime, timedelta

origins = ['DAL', 'LAX', 'ORD', 'ATL', 'DEN']
destinations = ['LAX', 'DAL', 'ATL', 'ORD', 'DEN']
statuses = ['On Time', 'Delayed', 'Cancelled']
weather = ['Clear', 'Rain', 'Thunderstorm', 'Fog', 'Cloudy']
aircrafts = ['Boeing 737', 'Airbus A320', 'Airbus A319']

def generate_data(num_rows=50):
    today = datetime.now().date()
    data = []
    for i in range(num_rows):
        origin = random.choice(origins)
        dest = random.choice([d for d in destinations if d != origin])
        dep_time = datetime.now().replace(hour=random.randint(0, 23), minute=random.choice([0, 15, 30, 45]))
        arr_time = dep_time + timedelta(hours=random.randint(1, 4))
        status = random.choice(statuses)
        delay = 0 if status == 'On Time' else random.choice([15, 30, 45, 60])
        delay = '' if status == 'Cancelled' else delay
        row = [
            f"AA{100 + i}",
            today.isoformat(),
            origin,
            dest,
            dep_time.strftime('%H:%M'),
            arr_time.strftime('%H:%M'),
            status,
            delay,
            random.choice(weather),
            random.choice(aircrafts)
        ]
        data.append(row)

    with open("flight_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['flight_id', 'flight_date', 'origin', 'destination', 'departure_time', 'arrival_time', 'status', 'delay_minutes', 'weather_condition', 'aircraft_type'])
        writer.writerows(data)

if __name__ == "__main__":
    generate_data()
