from fastapi import FastAPI
import requests
import feedparser
from fastapi.responses import HTMLResponse

app = FastAPI()

# Root
@app.get("/", response_class=HTMLResponse)
def root():
    return "<h2>✅ DailyBrief AI Backend is running</h2>"

# Weather
@app.get("/weather", response_class=HTMLResponse)
def weather(lat: float = 51.5072, lon: float = -0.1276):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto"
    weather_data = requests.get(weather_url).json()

    temp_max = weather_data["daily"]["temperature_2m_max"][0]
    temp_min = weather_data["daily"]["temperature_2m_min"][0]
    code = weather_data["daily"]["weathercode"][0]

    condition_map = {
        0: "Clear ☀️", 1: "Mainly Clear 🌤️", 2: "Cloudy ☁️", 3: "Overcast ☁️",
        45: "Fog 🌫️", 61: "Rain 🌧️", 80: "Heavy Rain ⛈️"
    }
    condition = condition_map.get(code, "Unknown")

    return f"<h3>🌦️ Weather Forecast</h3><p>{temp_max}°C / {temp_min}°C, {condition}</p>"

# News
@app.get("/news", response_class=HTMLResponse)
def news():
    feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")
    top_news = feed.entries[0]
    return f"<h3>📰 Top News</h3><p><a href='{top_news.link}' target='_blank'>{top_news.title}</a></p>"

# Missed Calls (placeholder)
@app.get("/missed-calls", response_class=HTMLResponse)
def missed_calls():
    return "<h3>📞 Missed Calls</h3><p>(Coming soon: Phone integration)</p>"

# Full Daily Brief
@app.get("/dailybrief", response_class=HTMLResponse)
def daily_brief(lat: float = 51.5072, lon: float = -0.1276):
    # Weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto"
    weather_data = requests.get(weather_url).json()
    temp_max = weather_data["daily"]["temperature_2m_max"][0]
    temp_min = weather_data["daily"]["temperature_2m_min"][0]
    code = weather_data["daily"]["weathercode"][0]

    condition_map = {
        0: "Clear ☀️", 1: "Mainly Clear 🌤️", 2: "Cloudy ☁️", 3: "Overcast ☁️",
        45: "Fog 🌫️", 61: "Rain 🌧️", 80: "Heavy Rain ⛈️"
    }
    condition = condition_map.get(code, "Unknown")

    # News
    feed = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")
    top_news = feed.entries[0]

    # Return HTML summary
    return f"""
        <h2>☀️ Daily Brief</h2>
        <p><b>Weather:</b> {temp_max}°C / {temp_min}°C, {condition}</p>
        <p><b>Top News:</b> <a href='{top_news.link}' target='_blank'>{top_news.title}</a></p>
        <p><b>Missed Calls:</b> Placeholder (to be integrated)</p>
    """

