from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_weather,
    get_weather,
)
from server.models.ow_data import (
    ResponseModel,
    OWData,
)
from server.models.wb_data import WBData

router = APIRouter()


# @router.post("/", response_description="Данные о погоде добавлены в базу данных")
# async def add_weather_data(data: OWData = Body(...)):
#     data = jsonable_encoder(data)
#     new_data = await add_weather(data)
#     return ResponseModel(new_data, "Успешное добавлено в базу данных.")


@router.get("/", response_description="Данные о погоде получены")
async def get_weather_data():
    weather_data = await get_weather()
    if weather_data:
        return ResponseModel(weather_data, "Данные о погоде успешно получены")
    return ResponseModel(weather_data, "Сервер вернул пустой список")
