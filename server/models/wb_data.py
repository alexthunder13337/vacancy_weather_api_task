from pydantic import BaseModel, Field


class WB_Weather(BaseModel):
    icon: str
    code: int
    description: str


class WB_Data(BaseModel):
    rh: int
    pod: str
    lon: float
    pres: float
    timezone: str
    ob_time: str
    county_code: str
    clouds: int
    ts: int
    solar_rad: int
    state_code: str
    city_name: str
    wind_spd: int
    wind_cdir_full: str
    wind_cdir: str
    spl: int
    vis: int
    h_angle: int
    sunset: str
    dni: int
    dewpt: int
    snow: int
    uv: int
    precip: int
    wind_dir: int
    sunrise: str
    ghi: int
    dhi: int
    aqi: int
    lat: float
    weather: WB_Weather
    datetime: str
    temp: int
    station: str
    elev_angle: float
    app_temp: float


class WBData(BaseModel):
    data: list[WB_Data]
    count: int
