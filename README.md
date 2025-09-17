# 🌍 DailyBrief AI Backend

This is the backend service for **DailyBrief AI**, providing:   
- 🌤️ Weather updates (via Open-Meteo API)  
- 📰 Trending news (via BBC RSS)  

## 🚀 Deployment  

### Local Run  
```bash
pip install -r requirements.txt
uvicorn app:app --reload
