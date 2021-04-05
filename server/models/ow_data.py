from pydantic import BaseModel, Field


class Coord(BaseModel):
    lon: float
    lat: float


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class Wind(BaseModel):
    speed: int
    deg: int


class Rain(BaseModel):
    hour: float = Field(alias='1h')


class Clouds(BaseModel):
    all: int


class Sys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int


class OWData(BaseModel):
    coord: Coord
    weather: list[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    rain: Rain = None
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

