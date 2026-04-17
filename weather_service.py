import requests

API_KEY = "a23c5c07aa355e1c6945a80a5803588b"

def get_weather(location: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        raise Exception("Invalid location")

    data = res.json()

    return {
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"]
    }