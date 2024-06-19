import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "country_code": response.get("country_code_iso3"),
        "country_capital": response.get("country_capital"),
        "isp": response.get("org"),
        "asn": response.get("asn"),
        "organization": response.get("org"),
        "postal": response.get("postal"),
        "utc_offset": response.get("utc_offset"),
        "continent": response.get("continent_code"),
        "currency": response.get("currency"),
        "languages": response.get("languages"),
    }
    return location_data

def get_weather(latitude, longitude):
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true').json()
    if 'current_weather' in response:
        weather_data = response['current_weather']
        weather = {
            "temperature": weather_data['temperature'],
            "wind_speed": weather_data['windspeed'],
            "condition": weather_data['weathercode']
        }
    else:
        weather = {
            "temperature": "Unknown",
            "wind_speed": "Unknown",
            "condition": "Unknown"
        }
    return weather

def get_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps/@{latitude},{longitude},10z"

def get_data(ip_address):
    location_data = get_location(ip_address)
    weather = get_weather(location_data["latitude"], location_data["longitude"])
    map_link = get_google_maps_link(location_data["latitude"], location_data["longitude"])

    # Prepare all information in a dictionary
    all_info = {
        "ip_address": ip_address,
        "map_link": map_link,
        "city": location_data["city"],
        "region": location_data["region"],
        "country": location_data["country"],
        "latitude": location_data["latitude"],
        "longitude": location_data["longitude"],
        "timezone": location_data["timezone"],
        "country_code": location_data["country_code"],
        "country_capital": location_data["country_capital"],
        "isp": location_data["isp"],
        "asn": location_data["asn"],
        "organization": location_data["organization"],
        "postal": location_data["postal"],
        "utc_offset": location_data["utc_offset"],
        "continent": location_data["continent"],
        "currency": location_data["currency"],
        "languages": location_data["languages"],
        "weather_condition": weather["condition"],
        "temperature": weather["temperature"],
        "wind_speed": weather["wind_speed"]
    }

    return all_info
