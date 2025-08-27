from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Alexandria"):
  
  requests_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
  
  weather_data = requests.get(requests_url).json()
  
  return weather_data

if __name__ == "__main__":
  print("\n*** Get Cerrent Weather Conditions***\n")
  
  city = input("Enter city name: ")
  
  # check for empty strings or only spacess
  
  if not bool(city.strip()):
    city = "Alexandria"
  
    
  weather_data = get_current_weather(city)
  
  print("\n")
  pprint(weather_data)
  
