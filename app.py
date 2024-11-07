from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

# Load weather data
def load_weather_data():
    data_file = os.path.join(os.path.dirname(__file__), "data", "weather_data.json")
    with open(data_file, "r") as f:
        return json.load(f)

@app.get("/")
def read_root():
    return {"message": "Weather Information Service"}

@app.get("/weather/{city}")
def get_weather(city: str):
    weather_data = load_weather_data()
    if city not in weather_data["cities"]:
        raise HTTPException(status_code=404, detail="City not found")
    return weather_data["cities"][city]

@app.get("/cities")
def get_cities():
    weather_data = load_weather_data()
    return list(weather_data["cities"].keys())
