# Import required modules 
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# Function to get weather information from OpenWeatherMap API
def get_weather(city):
    API_Key= "8eb56c5c8976ce7b01a4fd3ebbc0ecb3"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"

    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error" "City not found")
        return None

    # Parse the response JSON to get the weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp']
    description = weather['weather'][0]['description']
    wind_speed = weather['wind']['speed']
    humidity = weather['main']['humidity']
    city = weather['name']
    country = weather['sys']['country']

    # Get the icon URL and return all the weather information
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, wind_speed, humidity, city, country)

# Function to search weather for a city
def search():
    loading_label.pack(pady=10)  # Show the loading indicator
    root.update_idletasks()  # Force GUI update
    city = city_entry.get()
    result = get_weather(city)
    loading_label.pack_forget()  # Hide the loading indicator
    if result is None:
        return
    
    # If the city is found, unpack the weather information
    icon_url, temperature, description, wind_speed, humidity, city, country = result
    location_label.configure(text=f"{city}, {country}")
    
    # Get the weather icon image from URL and update the icon label
    image = Image.open(requests.get(icon_url, stream=True).raw)
    image = image.resize((150, 150)) 
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update the temperature, description, wind speed, and humiditylabels 
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")
    wind_speed_label.configure(text=f"Wind Speed: {wind_speed} m/s")
    humidity_label.configure(text=f"Humidity: {humidity}%")

#Create the main window
root = ttkbootstrap.Window(themename="solar")
root.title("Weather App")
root.geometry("850x850")

# Welcome Label
welcome_label = ttkbootstrap.Label(root, text="🌤️Welcome to the Weather App!", font=("Helvetica", 20), bootstyle="info")
welcome_label.pack(pady=20)  

# Prompt Label
prompt_label = ttkbootstrap.Label(root, text="Enter city name to search weather:", font=("Helvetica", 15), bootstyle="light")
prompt_label.pack(pady=10) 

# Entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font=("Helvetica, 18"), bootstyle="light", width=20)
city_entry.pack(pady=10)

# Loading Indicator
loading_label = ttkbootstrap.Label(root, text="Loading...", font=("Helvetica", 14), bootstyle="warning")
loading_label.pack_forget()  # Initially hidden

# Button widget -> to search for the weather information
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="success-outline")
search_button.pack(pady=10)

#Label widget -> to show the city/country name 
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Label widget -> to show the weather icon
icon_label = tk.Label(root)
icon_label.pack()

#Label widget -> to show the temperature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

#Label widget -> to show the weather description
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

# Label widget -> to show wind speed
wind_speed_label = tk.Label(root, font="Helvetica, 20")
wind_speed_label.pack()

# Label widget -> to show humidity
humidity_label = tk.Label(root, font="Helvetica, 20")
humidity_label.pack()

# Footer Section
footer_label = ttkbootstrap.Label( text="Created by: Amna Noor, Nusaiba Mumtaz, Irsa Attique, Adan Jamal",
                                   font=("Helvetica"), bootstyle="secondary")
footer_label.pack(side="bottom", pady=10)

# Start Tkinter event loop
root.mainloop( )
