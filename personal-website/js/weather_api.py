import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'city': data['name']
        }
    else:
        return None
