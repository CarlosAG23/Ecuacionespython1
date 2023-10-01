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