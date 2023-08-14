import requests

def get_location(city_name,country)->float:
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=cs&format=json"
    response = requests.get(url)

    if response.status_code == 200:
       city_data = response.json()
       city_location = city_data.get("results",{})
       city_name_data = city_location[0].get('name')
       country_name_data = city_location[0].get('country')
       latitude = city_location[0].get("latitude")
       longitude = city_location[0].get("longitude")
       print(f"Country: {country_name_data}")
       print(f"City: {city_name_data}")
       print(f"latitude: {latitude}")
       print(f"longitude: {longitude}")
       return latitude, longitude
    else:
       print("Error1")
       return None

def get_temperature(latitude, longitude)->float:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        current_weather = weather_data.get("current_weather", {})
        temperature = current_weather.get('temperature')
        print(f"Current temperature: {temperature}°C")
        return temperature
    else:
        print("Error2")
        return None

def store_temperature(temperature)->None:
    if temperature != None and temperature > 7:
        with open("temperature_data.txt", "r+") as file:
          value = int(file.read())
          file.seek(0)
          file.write(str(value + 1))

def main():

    country = "Česko"
    city_name = "Praha"
    latitude, longitude = get_location(city_name,country)
    ##latitude = 50.088
    ##longitude = 14.4208
    temperature = get_temperature(latitude, longitude)
    store_temperature(temperature)

if __name__ == "__main__":
    main()
