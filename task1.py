import requests
import matplotlib.pyplot as plt

# Replace with your actual API key
api_key = "open_weather_map_API_key"  # Make sure to replace this with your OpenWeatherMap API key
cities = ["Mumbai", "Odisha", "Bangalore", "Delhi", "Pune"]  # List of Indian cities
temperatures = []  # Empty list to store temperatures

# Fetch weather data for each city
for city in cities:
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        temperature_celsius = main_data['temp'] - 273.15  # Convert from Kelvin to Celsius
        temperatures.append(temperature_celsius)
    else:
        temperatures.append(None)  # In case the city is not found

# Create a bar chart to visualize the temperatures
plt.bar(cities, temperatures, color='blue')  # Bar chart with city names on x-axis and temperatures on y-axis
plt.xlabel("Cities")  # Label for x-axis
plt.ylabel("Temperature (°C)")  # Label for y-axis
plt.title("Temperature in Different Cities in India")  # Title of the chart
plt.show()  # Show the plot
