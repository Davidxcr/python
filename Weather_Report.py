#Web scraping forecast website with Python3
import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=42.004470000000026&lon=-88.10280999999998#.XzMLghNKg1I')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
weather_stuff = pd.DataFrame(
    {'Period': period_names,
    'Short_descriptions': short_descriptions,
    'Temperature': temperatures,
    })


print(weather_stuff)


weather_stuff.to_csv('weather_report.csv')
