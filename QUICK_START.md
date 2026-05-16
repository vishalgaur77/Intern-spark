# 🚀 API Integration - Quick Start Guide

## ⚡ 30-Second Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. (Optional) Add API Keys
Edit `api integration.py` and replace:
- Line 13: `WEATHER_API_KEY = "demo"` → Your OpenWeatherMap key
- Line 17: `NEWS_API_KEY = "demo"` → Your NewsAPI key
- CoinGecko (Line 15) needs no key!

### 3. Run the Script
```bash
python "api integration.py"
```

---

## 🔑 Get Free API Keys (2 minutes)

### Weather API
1. Go to: https://openweathermap.org/api
2. Sign up (free)
3. Copy your API Key
4. Paste in script line 13

### News API  
1. Go to: https://newsapi.org
2. Sign up (free)
3. Copy your API Key
4. Paste in script line 17

### Crypto API
✅ **No setup needed!** CoinGecko is completely free.

---

## 📱 Quick Operations

### Weather
```
Choose 1 → Weather API
Choose 1 → Enter city name → View weather
```

### Crypto (No setup needed!)
```
Choose 2 → Crypto API
Choose 1 → View top 5 cryptocurrencies
```

### News
```
Choose 3 → News API
Choose 1 → Select category → View headlines
```

---

## 🛠️ Troubleshooting

| Issue | Solution |
|---|---|
| ModuleNotFoundError: requests | Run `pip install requests` |
| API returns "invalid key" | Update API keys in script (lines 13, 17) |
| "Connection error" | Check internet connection |
| "Request timeout" | Server may be slow, try again |
| "Rate limit exceeded" | Wait a few minutes before next request |

---

## 📊 Features Quick Reference

| Feature | Where |
|---|---|
| Get Weather | Menu 1 |
| Crypto Prices | Menu 2 |
| News Headlines | Menu 3 |
| Price Filters | Crypto → Option 3 |
| News Search | News → Option 2 |
| Source Filter | News → Option 3 |
| View Logs | Open `api_logs.txt` |

---

## 💻 System Requirements

- Python 3.6+
- Internet connection
- ~5MB disk space
- Requests library

---

## 📞 Support Links

- **OpenWeatherMap**: https://openweathermap.org/api
- **CoinGecko**: https://www.coingecko.com/api  
- **NewsAPI**: https://newsapi.org
- **Requests Docs**: https://docs.python-requests.org/

---

## ✅ What's Logged

Everything is saved to `api_logs.txt`:
- ✅ Successful API calls
- ❌ Errors and failures
- ⏱️ Timestamps for all operations
- 📊 Data retrieved counts

Check logs for debugging or audit trail!

---

## 🎓 Code Highlights

**Safe JSON parsing:**
```python
price = data.get("bitcoin", {}).get("usd", 0)
```

**Exception handling:**
```python
try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout:
    # Handle gracefully
```

**Smart filtering:**
```python
filtered = [crypto for crypto in data if min_price <= crypto['price'] <= max_price]
```

---

Enjoy exploring APIs! 🎉
