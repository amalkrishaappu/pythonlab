import json
import pandas as pd

# Sample JSON weather data
weather_data = '''
{
    "cities": [
        {
            "location": "Chennai",
            "weather": {
                "temperature": 32,
                "humidity": 70
            }
        },
        {
            "location": "Delhi",
            "weather": {
                "temperature": 28,
                "humidity": 60
            }
        },
        {
            "location": "Mumbai",
            "weather": {
                "temperature": 30,
                "humidity": 80
            }
        }
    ]
}
'''

# Parse JSON data
data = json.loads(weather_data)

# Extract weather details
records = []

for city in data["cities"]:
    records.append({
        "City": city["location"],
        "Temperature": city["weather"]["temperature"],
        "Humidity": city["weather"]["humidity"]
    })

# Convert JSON data into tabular format
df = pd.DataFrame(records)

# Display weather table
print("Weather Information:")
print(df)

# Display summarized weather report
print("\nWeather Report:")
print("Total Cities:", len(df))
print("Average Temperature:", df["Temperature"].mean())
print("Average Humidity:", df["Humidity"].mean())

# Display city-wise details
for index, row in df.iterrows():
    print("\nCity:", row["City"])
    print("Temperature:", row["Temperature"], "°C")
    print("Humidity:", row["Humidity"], "%")