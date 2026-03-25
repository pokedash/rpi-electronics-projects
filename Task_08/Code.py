import adafruit_dht
import board
import time
import os
import csv
from datetime import datetime

DHT_PIN = board.D4
LOG_FILE = 'sensor_log.csv'
READ_INTERVAL = 10 #seconds between readings

dht_sensor = adafruit_dht.DHT11(DHT_PIN)

def calculate_heat_index(temp_c, humidity):
    """Calculate the heat index in Celsius using the formula from NOAA"""
    temp_f = temp_c * 9/5 + 32
    hi_f = -42.379 + 2.04901523*temp_f + 10.14333127*humidity - 0.22475541*temp_f*humidity - 0.00683783*temp_f**2 - 0.05481717*humidity**2 + 0.00122874*temp_f**2*humidity + 0.00085282*temp_f*humidity**2 - 0.00000199*temp_f**2*humidity**2
    hi_c = (hi_f - 32) * 5/9
    return hi_c

def init_csv():
    """Initialize the CSV log file with headers if it doesn't exist"""
    if not os.path.isfile(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Temperature (C)', 'Humidity (%)', 'Heat Index (C)'])

        print(f'Created log file: {LOG_FILE}')
    else:
        print(f'Appending to existing log: {LOG_FILE}')

def log_reading(temp, humidity):
    """Log the sensor reading to the CSV file"""
    heat_index = calculate_heat_index(temp, humidity)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, f'{temp:.1f}', f'{humidity:.1f}', f'{heat_index:.1f}'])

    print(f'Logged: {timestamp} | Temp: {temp:.1f} C | Humidity: {humidity:.1f}% | Heat Index: {heat_index:.1f} C')

# -------------- Main 
init_csv()
print(f'Logging every {READ_INTERVAL} seconds to {LOG_FILE}. Press Ctrl+C to stop.')
reading_count = 0

try:
    while True:
        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            log_reading(temperature, humidity)
            reading_count += 1

        except RuntimeError as e:
            print(f'Read failed: {e} - skipping this reading')
            

        time.sleep(READ_INTERVAL)

except KeyboardInterrupt:
    print(f'\nLogged {reading_count}: readings to {LOG_FILE}')

finally:
    dht_sensor.exit()