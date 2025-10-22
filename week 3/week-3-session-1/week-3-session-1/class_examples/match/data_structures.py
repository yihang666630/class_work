# Example list of sensor data: (sensor_type, value)
# You will see more of lists and tuples next week!
sensor_data = [
    ("temperature", 75.0),
    ("humidity", 55),
    ("pressure", 1015),
    ("temperature", 100.0),  # Too hot!
    ("humidity", 25),         # Too low!
    ("pressure", 990),        # Too low!
]
#print (sensor_data)

# Process each tuple in the sensor_data list
for data in sensor_data:
    match data:
        case ("temperature", temp):
            if temp > 90:
                print(f"Warning! High temperature detected: {temp}°C")
            else:
                print(f"Temperature is normal: {temp}°C")
        
        case ("humidity", hum):
            if hum < 30:
                print(f"Low humidity level detected: {hum}%")
            else:
                print(f"Humidity level is normal: {hum}%")
        
        case ("pressure", pres):
            if pres < 1000:
                print(f"Low pressure detected: {pres} hPa")
            else:
                print(f"Pressure level is normal: {pres} hPa")
        
        case _:
            print("Unknown sensor data")
