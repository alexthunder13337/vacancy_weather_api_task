import motor.motor_asyncio
from bson.objectid import ObjectId
import urllib.request
import json

OW_API_KEY = '23ab6dbcfcff58a730b9411b21c6f5dc'

WB_API_KEY = '2d5e36f5407a4181a5ddb2be1feeb56e'

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.Weather

ow_collection = database.get_collection("OpenWeather")
wb_collection = database.get_collection("WeatherBit")


# helpers


def ow_weather_helper(ow_weather) -> dict:
    return {
        "_id": str(ow_weather["_id"]),
        "coord": ow_weather["coord"],
        "weather": ow_weather["weather"],
        "base": ow_weather["base"],
        "main": ow_weather["main"],
        "visibility": ow_weather["visibility"],
        "wind": ow_weather["wind"],
        "clouds": ow_weather["clouds"],
        "dt": ow_weather["dt"],
        "sys": ow_weather["sys"],
        "timezone": ow_weather["timezone"],
        "id": ow_weather["id"],
        "name": ow_weather["name"],
        "cod": ow_weather["cod"],
        "from": "OpenWeather",
    }


def wb_weather_helper(wb_weather) -> dict:
    return {
        "_id": str(wb_weather["_id"]),
        "data": wb_weather["data"],
        "count": wb_weather["count"],
        "service_from": "WeatherBit",
    }


async def get_weather():
    city = 'Moscow'
    ow_weather = []
    wb_weather = []
    ow_api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OW_API_KEY}&units=metric&lang=ru'
    ow_url = urllib.request.urlopen(ow_api_url)
    ow_data = json.loads(ow_url.read())
    ow_weather_new = await ow_collection.insert_one(ow_data)
    async for owdata in ow_collection.find():
        ow_weather.append(ow_weather_helper(owdata))
    city_id = '524901'
    wb_api_url = f'https://api.weatherbit.io/v2.0/current?city_id={city_id}&lang=ru&key={WB_API_KEY}'
    wb_url = urllib.request.urlopen(wb_api_url)
    wb_data = json.loads(wb_url.read())
    wb_weather_new = await wb_collection.insert_one(wb_data)
    async for wbdata in wb_collection.find():
        wb_weather.append(wb_weather_helper(wbdata))

    return ow_weather, wb_weather


# Add a new weather data into to the database
async def add_weather(weather_data: dict) -> dict:
    weather = await ow_collection.insert_one(weather_data)
    new_weather = await ow_collection.find_one({"_id": weather.inserted_id})
    return ow_weather_helper(new_weather)
