import requests
from datetime import datetime, timedelta
from telegram import Bot
import asyncio
import emoji

# Configuración
telegram_token = 'TU_TOKEN_DE_TELEGRAM'
weather_api_key = 'TU_API_KEY_DE_OPENWEATHERMAP'
city_name = 'Quito'
chat_id = 'your_id'
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

# Función para enviar mensaje a Telegram
async def send_telegram_message(message):
    bot = Bot(token=telegram_token)
    await bot.send_message(chat_id=chat_id, text=message)

# Función principal
async def main():
    while True:
        now = datetime.now()

        # Verifica si hoy es sábado (día de la semana 5 en la convención ISO)
        if now.weekday() == 5:
            target_time = datetime(now.year, now.month, now.day, target_hour, target_minute, 0)

            # Si la hora actual es igual o después de la hora deseada
            if now >= target_time:
                target_time += timedelta(days=7)

            time_to_wait = target_time - now
            seconds_to_wait = time_to_wait.total_seconds()

            # Espera hasta la hora deseada
            if seconds_to_wait > 0:
                print(f"Esperando {seconds_to_wait} segundos hasta las {target_hour}:{target_minute}...")
                await asyncio.sleep(seconds_to_wait)

            # Obtiene el pronóstico del tiempo
            weather_info = get_weather()

            # Envia el mensaje a Telegram
            await send_telegram_message(weather_info)

            # Calcula el tiempo hasta la próxima hora deseada
            next_target_time = target_time + timedelta(hours=1)
            time_to_wait_next_hour = next_target_time - datetime.now()
            seconds_to_wait_next_hour = max(time_to_wait_next_hour.total_seconds(), 0)

            # Espera hasta la próxima hora deseada
            await asyncio.sleep(seconds_to_wait_next_hour)
        else:
            # Si no es sábado, espera hasta el próximo sábado
            next_saturday = now + timedelta(days=(5 - now.weekday() + 7) % 7)
            time_to_wait = next_saturday - now
            seconds_to_wait = time_to_wait.total_seconds()

            # Espera hasta el próximo sábado
            print(f"Hoy no es sábado. Esperando {seconds_to_wait} segundos hasta el próximo sábado...")
            await asyncio.sleep(seconds_to_wait)
if __name__ == "__main__":
    asyncio.run(main())