#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'][:10] == date:
                return item['main']['temp']
        return None
    else:
        return None

def get_wind_speed(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'][:10] == date:
                return item['wind']['speed']
        return None
    else:
        return None

def get_pressure(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for item in data['list']:
            if item['dt_txt'][:10] == date:
                return item['main']['pressure']
        return None
    else:
        return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_weather_data(date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} K")
            else:
                print("Data not found for the given date.")
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date.")
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the given date.")
        elif option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




