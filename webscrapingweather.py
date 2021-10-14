import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get ("https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.YWekpUbMK3I")
soup = BeautifulSoup(page.content,"html.parser")
week = soup.find(id="seven-day-forecast")
#print (week)
  
items = (week.find_all(class_= "tombstone-container"))
#print(items[0])

#print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_description)
#print(temperature)
 
weather_item = pd.DataFrame(
     {
         'period': period_names,
         'short_description': short_description,
        'temperature' : temperature,
        })

print(weather_item)

weather_item.to_csv('weather.csv')