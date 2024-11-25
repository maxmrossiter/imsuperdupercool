import requests

def get_random_activity():
    base_url = "https://www.boredapi.com/api/activity"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data['activity']
    else:
        return "Could not fetch activity at this time."
