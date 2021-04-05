from fastapi import FastAPI
import webbrowser

from server.routes.weather import router as WeatherRouter

webbrowser.open('http://localhost:8000/docs', new=2)
app = FastAPI()

app.include_router(WeatherRouter, tags=["Weather"], prefix="/weather")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Данные о погоде с OpenWeather и WeatherBit"}
