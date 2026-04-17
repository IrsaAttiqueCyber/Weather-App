# Weather-App
Project Overview
This Weather App is a desktop application developed in Python that provides real-time weather updates for any city globally. It features a modern, professional user interface (UI) and retrieves live data using the OpenWeatherMap API.
The project demonstrates the integration of external APIs with a graphical front-end, focusing on both functional accuracy and visual presentation.
Features
Real-Time Data: Fetches current temperature, weather conditions (description), wind speed, and humidity.
Visual Icons: Dynamically displays weather icons (e.g., sun, clouds, rain) corresponding to the current conditions.
Modern UI: Built with ttkbootstrap to provide a sleek, "success-outline" themed interface with custom typography.
Error Handling: Includes validation to alert the user if a city is not found or if there are connectivity issues.
Loading State: Features a loading indicator to improve the user experience during data retrieval.
Technical Stack
Language: Python 3
GUI Framework: tkinter (Base) & ttkbootstrap (Theming)
API Integration: requests library for communicating with the OpenWeatherMap API.
Image Processing: PIL (Pillow) for handling and displaying weather icons.
How It Works
User Input: The user enters a city name into the search field.
API Call: The app sends a request to the OpenWeatherMap API using a unique API Key.
Data Parsing: The JSON response is parsed to extract specific metrics like temperature (in Celsius) and humidity.
UI Update: The application updates the labels and fetches the appropriate weather icon to display to the user.
Setup Instructions
Install Dependencies:
Bash
pip install requests pillow ttkbootstrap
API Key: The project currently uses a built-in API key. For personal use or higher limits, you can obtain your own from OpenWeatherMap.
Run the App:
Bash
python "WEATHER APP.py"
Developer: Irsa Attique
Focus: UI/UX Design & API Integration
