from celery import shared_task
import requests
import logging
from . import models

api_key = "2011750bdcb7475e85484928242402"


logger = logging.getLogger(__name__)


@shared_task
def update_country_weather():
    countries = models.Country.objects.all()
    for country in countries:
        try:
            response = requests.get(
                f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={country.capital}"
            )
            if response.status_code == 200:
                data = response.json()
                country.temperature = data["current"]["temp_c"]
                country.humidity = data["current"]["humidity"]
                country.uv_index = data["current"]["uv"]
                country.save()
            else:
                logger.error(
                    f"Failed to fetch weather data for {country.name}: {response.status_code}"
                )
        except Exception as e:
            logger.error(f"Error updating weather for {country.capital}: {e}")
