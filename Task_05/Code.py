import adafruit_dht
import board
import time

dht_sensor = adafruit_dht.DHT11(board.D4)

print("Task 05: DHT11 Temperature and Humidity Sensor. Ctrl+C to stop")
print(f"{'Timestamp':<20} {'Temperature (C)':>15} {'Humidity (%)':>12}")
print('-'*50)

try:
    while True:
        try:
            temperature = dht_sensor.temperature    #Degrees celsius
            humidity = dht_sensor.humidity          #Relative humidity in percentage

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"{timestamp:<20} {temperature:>15.1f} {humidity:>12.1f}")
        except RuntimeError as e:
            print(f"Error reading DHT11 sensor: {e}")
            
        time.sleep(2)

except KeyboardInterrupt:
    print('/nStopped')

finally:
    dht_sensor.exit() #Clean up resources used by the sensor