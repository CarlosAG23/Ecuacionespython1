import requests
from datetime import datetime, timedelta
from telegram import Bot
import asyncio
import emoji

# Configuración
telegram_token = 'TU_TOKEN_DE_TELEGRAM'
weather_api_key = 'TU_API_KEY_DE_OPENWEATHERMAP'
city_name = 'Quito'
chat_id = '348562795'
target_hour = 21
target_minute = 31  # Cambia a 10 para 20:10

# Función para obtener el pronóstico del tiempo
def get_weather():
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': weather_api_key, 'units': 'metric', 'lang': 'es'}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        weather_emoji = get_weather_emoji(weather_description)
        return f"Hola, Carlos. Soy Weather Bot y este es el pronóstico del tiempo para hoy:\n\n" \
               f"{emoji.emojize(':cityscape:')} Ciudad: {city}\n" \
               f"{emoji.emojize(':thermometer:')} Temperatura: {temperature}°C\n" \
               f"{weather_emoji} Estado del tiempo: {weather_description}"
    else:
        return f"Error al obtener el pronóstico: {response.json()['message']}"

# Función para obtener un emoji basado en la descripción del clima
def get_weather_emoji(weather_description):
    if 'lluvia' in weather_description.lower():
        return emoji.emojize(':umbrella_with_rain_drops:')
    elif 'sol' in weather_description.lower():
        return emoji.emojize(':sunny:')
    elif 'nube' in weather_description.lower():
        return emoji.emojize(':cloud:')
    else:
        return ''
