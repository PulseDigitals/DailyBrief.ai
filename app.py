from fastapi import FastAPI
import requests
import feedparser

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DailyBrief AI Backend is running 🚀"}

@app.get("/dailybrief")
def daily_brief(lat: float = 51.5072, lon: float = -0.1276):
    # Weather API
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto"
    weather_data = requests.get(weather_url).json()
    temp_max = weather_data["daily"]["temperature_2m_max"][0]
    temp_min = weather_data["daily"]["temperature_2m_min"][0]
    code = weather_data["daily"]["weathercode"][0]

    # Weather code map
    condition_map = {
        0: "Clear ☀️", 1: "Mainly Clear 🌤️", 2: "Cloudy ☁️", 3: "Overcast 🌥️",
        45: "Fog 🌫️", 61: "Rain 🌧️", 80: "Heavy Rain ⛈️"
    }
    condition = condition_map.get(code, "Unknown")

    # News (BBC RSS)
    feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")
    top_news = feed.entries[0]
    headline = top_news.title
    link = top_news.link

    return {
        "weather": f"{temp_max}°C/{temp_min}°C, {condition}",
        "headline": headline,
        "url": link
    }
