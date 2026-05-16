# API Integration Project - Complete Documentation

## 📋 Overview
This is a comprehensive API integration script that fetches data from Weather, Crypto, and News APIs with proper JSON parsing, error handling, and filtering capabilities.

---

## ✨ Features Implemented

✅ **Requests Module** - HTTP requests to multiple APIs  
✅ **JSON Parsing** - Extracts and parses API responses  
✅ **Search/Filter** - Multiple filtering options per API  
✅ **Error Handling** - Exception handling for network errors, timeouts, rate limits  
✅ **Logging System** - Logs all API calls to api_logs.txt  
✅ **Interactive Menu** - User-friendly interface with submenus  

---

## 🚀 Installation & Setup

### 1. **Install Required Package**
```bash
pip install requests
```

### 2. **Get API Keys (Free)**

#### Weather API (OpenWeatherMap)
- Visit: https://openweathermap.org/api
- Sign up for free account
- Get free API key
- Replace `WEATHER_API_KEY = "demo"` in script

#### Crypto API (CoinGecko)
- **No API key required!** (Public API)
- Works immediately without setup

#### News API (NewsAPI)
- Visit: https://newsapi.org
- Sign up for free account
- Get free API key (100 requests/day)
- Replace `NEWS_API_KEY = "demo"` in script

---

## 📊 Sample Input/Output Scenarios

### **Scenario 1: Weather API - Get City Weather**

**INPUT:**
```
==================================================
🌐 API INTEGRATION PROJECT
==================================================

📋 Choose an API:
  1. 🌍 Weather API
  2. 💰 Crypto API
  3. 📰 News API
  4. ❓ Get API Information
  5. 🚪 Exit
==================================================

👉 Enter your choice (1-5): 1

==================================================
🌍 WEATHER API MENU
==================================================

🔧 Choose an option:
  1. Get weather by city
  2. Get weather in Celsius
  3. Get weather in Fahrenheit
  4. Back to main menu
==================================================

👉 Enter your choice (1-4): 1
🏙️  Enter city name: London
```

**OUTPUT:**
```
🌍 Fetching weather for London...

==================================================
🌤️  WEATHER INFORMATION
==================================================

📍 Location: London, GB
🌡️  Temperature: 15.2°C (feels like 14.8°C)
💧 Humidity: 72%
🌪️  Wind Speed: 4.5 m/s
⚡ Pressure: 1013 hPa
📝 Condition: Overcast clouds

==================================================
```

**API Response (JSON):**
```json
{
  "coord": {"lon": -0.1257, "lat": 51.5085},
  "weather": [
    {"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}
  ],
  "main": {
    "temp": 15.2,
    "feels_like": 14.8,
    "humidity": 72,
    "pressure": 1013
  },
  "wind": {"speed": 4.5},
  "name": "London",
  "sys": {"country": "GB"}
}
```

**LOG ENTRY (api_logs.txt):**
```
[2026-05-16 14:30:15] Weather API - SUCCESS - City: London
```

---

### **Scenario 2: Weather API - Fahrenheit Conversion**

**INPUT:**
```
👉 Enter your choice (1-4): 3
🏙️  Enter city name: New York
```

**OUTPUT:**
```
🌍 Fetching weather for New York...

==================================================
🌤️  WEATHER INFORMATION
==================================================

📍 Location: New York, US
🌡️  Temperature: 68.5°F (feels like 66.2°F)
💧 Humidity: 65%
🌪️  Wind Speed: 3.2 m/s
⚡ Pressure: 1015 hPa
📝 Condition: Partly cloudy

==================================================
```

---

### **Scenario 3: Crypto API - Top 5 Cryptocurrencies**

**INPUT:**
```
👉 Enter your choice (1-5): 2

==================================================
💰 CRYPTO API MENU
==================================================

🔧 Choose an option:
  1. Get top 5 cryptocurrencies
  2. Search specific cryptocurrencies
  3. Filter by price range
  4. Back to main menu
==================================================

👉 Enter your choice (1-4): 1
```

**OUTPUT:**
```
💰 Fetching crypto prices for: bitcoin, ethereum, cardano, solana, ripple...

================================================================================
💰 CRYPTOCURRENCY PRICES (USD)
================================================================================
Cryptocurrency       Price            Market Cap           24h Change
--------------------------------------------------------------------------------
Bitcoin              USD 45,230.50    USD 884,234,500,000  📈 +2.35%
Ethereum             USD 2,540.75     USD 305,432,100,000  📈 +1.85%
Cardano              USD 0.52         USD 18,234,560,000   📉 -0.45%
Solana               USD 105.30       USD 43,210,500,000   📈 +3.12%
Ripple               USD 0.85         USD 44,532,100,000   📉 -1.20%
================================================================================
```

**API Response (JSON):**
```json
{
  "bitcoin": {
    "usd": 45230.50,
    "usd_market_cap": 884234500000,
    "usd_24h_change": 2.35
  },
  "ethereum": {
    "usd": 2540.75,
    "usd_market_cap": 305432100000,
    "usd_24h_change": 1.85
  },
  "cardano": {
    "usd": 0.52,
    "usd_market_cap": 18234560000,
    "usd_24h_change": -0.45
  },
  "solana": {
    "usd": 105.30,
    "usd_market_cap": 43210500000,
    "usd_24h_change": 3.12
  },
  "ripple": {
    "usd": 0.85,
    "usd_market_cap": 44532100000,
    "usd_24h_change": -1.20
  }
}
```

**LOG ENTRY:**
```
[2026-05-16 14:35:20] Crypto API - SUCCESS - Fetched 5 cryptocurrencies
```

---

### **Scenario 4: Crypto API - Search Specific Cryptocurrencies**

**INPUT:**
```
👉 Enter your choice (1-4): 2
🔍 Enter crypto IDs (comma-separated, e.g., bitcoin,ethereum,ripple): polkadot,dogecoin,litecoin
```

**OUTPUT:**
```
💰 Fetching crypto prices for: polkadot, dogecoin, litecoin...

================================================================================
💰 CRYPTOCURRENCY PRICES (USD)
================================================================================
Cryptocurrency       Price            Market Cap           24h Change
--------------------------------------------------------------------------------
Polkadot             USD 8.45         USD 10,230,500,000   📈 +1.23%
Dogecoin             USD 0.15         USD 21,432,100,000   📉 -0.85%
Litecoin             USD 95.50        USD 12,543,210,000   📈 +2.05%
================================================================================
```

---

### **Scenario 5: Crypto API - Filter by Price Range**

**INPUT:**
```
👉 Enter your choice (1-4): 3
💵 Enter minimum price: 0.5
💵 Enter maximum price: 50
```

**OUTPUT:**
```
💰 Fetching crypto prices for: bitcoin, ethereum, cardano, solana, ripple...

================================================================================
💰 CRYPTOCURRENCY PRICES (USD)
================================================================================
Cryptocurrency       Price            Market Cap           24h Change
--------------------------------------------------------------------------------
Solana               USD 28.45        USD 12,543,210,000   📈 +2.15%
Ripple               USD 5.85         USD 44,532,100,000   📉 -1.20%
Cardano              USD 15.52        USD 18,234,560,000   📈 +0.45%
================================================================================
```

---

### **Scenario 6: News API - Top Headlines by Category**

**INPUT:**
```
👉 Enter your choice (1-5): 3

==================================================
📰 NEWS API MENU
==================================================

🔧 Choose an option:
  1. Top headlines by category
  2. Search news by keyword
  3. Filter by source
  4. Back to main menu
==================================================

👉 Enter your choice (1-4): 1

📂 Categories: business, entertainment, general, health, science, sports, technology
📂 Enter category (default: general): technology
```

**OUTPUT:**
```
📰 Fetching technology news...

====================================================================================================
📰 NEWS ARTICLES (Showing 5 of 142)
====================================================================================================

📌 Article 1
   📢 Source: TechCrunch
   📝 Title: OpenAI Releases GPT-5 with Revolutionary Capabilities
   📄 Description: OpenAI announced today the launch of GPT-5, featuring advanced reasoning and multimodal capabilities that surpass previous models. The model demonstrates 40% improvement in complex problem-solving...
   🔗 URL: https://techcrunch.com/news/openai-gpt5-release
   ⏰ Published: 2026-05-16 12:30:45
----------------------------------------------------------------------------------------------------

📌 Article 2
   📢 Source: The Verge
   📝 Title: Apple Announces iPhone 17 with Revolutionary AI Features
   📄 Description: Apple has unveiled its latest flagship smartphone with cutting-edge AI integration for photography and personal assistance. The new device features a custom neural engine designed specifically...
   🔗 URL: https://theverge.com/news/iphone17
   ⏰ Published: 2026-05-16 11:15:30
----------------------------------------------------------------------------------------------------

📌 Article 3
   📢 Source: CNN Tech
   📝 Title: AI Regulations Take Shape in EU Parliament
   📄 Description: The European Parliament has passed landmark legislation aimed at regulating artificial intelligence systems. The new framework emphasizes transparency and accountability for high-risk AI applications...
   🔗 URL: https://cnn.com/tech/ai-regulations
   ⏰ Published: 2026-05-16 10:45:00
----------------------------------------------------------------------------------------------------

📌 Article 4
   📢 Source: Wired
   📝 Title: Quantum Computing Breakthrough Achieves 1000-Qubit Milestone
   📄 Description: Researchers announce a major breakthrough in quantum computing, successfully scaling systems to 1000 qubits. This milestone brings practical quantum computers closer to reality for solving real-world problems...
   🔗 URL: https://wired.com/story/quantum-breakthrough
   ⏰ Published: 2026-05-16 09:20:15
----------------------------------------------------------------------------------------------------

📌 Article 5
   📢 Source: Ars Technica
   📝 Title: NASA's New Rover Discovers Water on Mars Subsurface
   📄 Description: NASA's latest rover has detected significant water deposits beneath Mars' surface using advanced ground-penetrating radar. Scientists believe this discovery could be crucial for future human missions...
   🔗 URL: https://arstechnica.com/nasa-mars-water
   ⏰ Published: 2026-05-16 08:00:00
====================================================================================================
```

**API Response (JSON) - Sample Article:**
```json
{
  "articles": [
    {
      "source": {"id": "techcrunch", "name": "TechCrunch"},
      "author": "John Smith",
      "title": "OpenAI Releases GPT-5 with Revolutionary Capabilities",
      "description": "OpenAI announced today the launch of GPT-5, featuring advanced reasoning and multimodal capabilities...",
      "url": "https://techcrunch.com/news/openai-gpt5-release",
      "urlToImage": "https://example.com/image.jpg",
      "publishedAt": "2026-05-16T12:30:45Z",
      "content": "Full article content here..."
    }
  ],
  "totalResults": 142,
  "status": "ok"
}
```

**LOG ENTRY:**
```
[2026-05-16 14:40:00] News API - SUCCESS - Found 142 articles
```

---

### **Scenario 7: News API - Search News by Keyword**

**INPUT:**
```
👉 Enter your choice (1-4): 2
🔍 Enter search keyword: machine learning
```

**OUTPUT:**
```
📰 Searching news for: machine learning...

====================================================================================================
📰 NEWS ARTICLES (Showing 5 of 1,243)
====================================================================================================

📌 Article 1
   📢 Source: MIT News
   📝 Title: Machine Learning Model Predicts Protein Structures with 99% Accuracy
   📄 Description: Researchers at MIT have developed a machine learning model that can predict 3D protein structures with unprecedented accuracy. This breakthrough could accelerate drug discovery and development...
   🔗 URL: https://mitnews.com/ml-protein-prediction
   ⏰ Published: 2026-05-16 14:00:00
----------------------------------------------------------------------------------------------------

[Additional articles...]

====================================================================================================
```

---

### **Scenario 8: News API - Filter by Source**

**INPUT:**
```
👉 Enter your choice (1-4): 3
🏢 Enter source name to filter: BBC News
```

**OUTPUT:**
```
📰 Fetching general news...

====================================================================================================
📰 NEWS ARTICLES (Showing 3 of 3)
====================================================================================================

📌 Article 1
   📢 Source: BBC News
   📝 Title: Global Markets React to Economic Data
   📄 Description: Financial markets showed mixed results today following the release of key economic indicators...
   🔗 URL: https://bbc.com/news/business
   ⏰ Published: 2026-05-16 15:30:00
----------------------------------------------------------------------------------------------------

[Additional BBC articles...]

====================================================================================================
```

---

### **Scenario 9: Error Handling - Invalid City**

**INPUT:**
```
👉 Enter your choice (1-5): 1
👉 Enter your choice (1-4): 1
🏙️  Enter city name: XyZ12345InvalidCity
```

**OUTPUT:**
```
🌍 Fetching weather for XyZ12345InvalidCity...

❌ Weather API: Resource not found (404)
```

**LOG ENTRY:**
```
[2026-05-16 14:45:30] Weather API - ERROR - Resource not found (404)
```

---

### **Scenario 10: Error Handling - Connection Timeout**

**OUTPUT:**
```
❌ Weather API: Request timeout
```

**LOG ENTRY:**
```
[2026-05-16 14:46:45] Weather API - ERROR - Request timeout
```

---

### **Scenario 11: Error Handling - Invalid API Key**

**OUTPUT:**
```
❌ News API: Invalid API key (401)
```

**LOG ENTRY:**
```
[2026-05-16 14:47:00] News API - ERROR - Invalid API key (401)
```

---

### **Scenario 12: API Information Display**

**INPUT:**
```
👉 Enter your choice (1-5): 4
```

**OUTPUT:**
```
================================================================================
ℹ️  API INFORMATION
================================================================================

🌍 WEATHER API (OpenWeatherMap)
--------------------------------------------------------------------------------
  Website: https://openweathermap.org/api
  Features: Real-time weather, forecasts, historical data
  Free Tier: Up to 1000 calls/day
  Setup: Get free API key from openweathermap.org
  Parameters: City, Country code, Units (metric/imperial)

💰 CRYPTO API (CoinGecko)
--------------------------------------------------------------------------------
  Website: https://www.coingecko.com/api
  Features: Cryptocurrency prices, market data, historical data
  Free Tier: Unlimited requests (public)
  Setup: No API key required!
  Parameters: Crypto IDs, Currency, Time period

📰 NEWS API (NewsAPI)
--------------------------------------------------------------------------------
  Website: https://newsapi.org
  Features: Top headlines, search articles, filters by category
  Free Tier: Up to 100 requests/day
  Setup: Get free API key from newsapi.org
  Parameters: Keywords, Category, Country, Sort order

================================================================================
```

---

## 📝 Sample Log File (api_logs.txt)

```
[2026-05-16 14:00:00] SYSTEM - START - API Integration program started
[2026-05-16 14:30:15] Weather API - SUCCESS - City: London
[2026-05-16 14:35:20] Crypto API - SUCCESS - Fetched 5 cryptocurrencies
[2026-05-16 14:40:00] News API - SUCCESS - Found 142 articles
[2026-05-16 14:45:30] Weather API - ERROR - Resource not found (404)
[2026-05-16 14:46:45] Weather API - ERROR - Request timeout
[2026-05-16 14:47:00] News API - ERROR - Invalid API key (401)
[2026-05-16 14:50:00] News API - SUCCESS - Found 1243 articles
[2026-05-16 15:00:00] SYSTEM - END - API Integration program ended
```

---

## 🎯 Key Features Explained

### **1. Requests Module Integration**
```python
response = requests.get(url, params=params, timeout=5)
```
- Makes HTTP GET requests to APIs
- Handles timeouts gracefully
- Supports query parameters

### **2. JSON Parsing**
```python
data = response.json()
price = data.get("bitcoin", {}).get("usd", 0)
```
- Converts API responses to Python dictionaries
- Safe access with `.get()` method
- Prevents KeyError exceptions

### **3. Filtering & Search**
```python
# Price range filter
if min_price <= price <= max_price:
    filtered[crypto] = prices

# Source filter
filtered = [article for article in articles 
            if article.get("source", {}).get("name") == source_name]

# Keyword search
if keyword in article.get("title", "").lower():
    results.append(article)
```

### **4. Error Handling**
```python
try:
    response = requests.get(url, params=params, timeout=5)
except requests.exceptions.Timeout:
    print("Request timeout")
except requests.exceptions.ConnectionError:
    print("Connection error")
```

### **5. Logging System**
```python
def log_api_call(api_name, status, message):
    with open("api_logs.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {api_name} - {status} - {message}\n")
```

---

## 📋 Requirements Met

| Requirement | Status | Details |
|---|---|---|
| Use requests module | ✅ | HTTP requests to 3 different APIs |
| Parse JSON response | ✅ | Extracts nested JSON data safely |
| Add search/filter | ✅ | 8+ filtering options across APIs |
| Error handling | ✅ | Network errors, timeouts, rate limits |
| User interaction | ✅ | Interactive menus with submenus |
| Logging | ✅ | All operations logged with timestamps |

---

## 🚀 How to Run

```bash
python "api integration.py"
```

Then choose an API and select operations from the interactive menu.

---

## 💡 Advanced Usage

### **Get Weather for Multiple Cities**
1. Select Weather API → Weather in Celsius
2. Enter city name
3. Repeat for different cities

### **Compare Cryptocurrency Prices**
1. Select Crypto API → Get top 5
2. Takes note of prices
3. Later filter by price range to see changes

### **Track Specific News Sources**
1. Select News API → Search news
2. Enter keyword
3. Later filter by source to get articles from specific outlet

---

## ⚠️ Important Notes

- **API Keys**: Update `WEATHER_API_KEY` and `NEWS_API_KEY` after getting free keys
- **Rate Limits**: Free tier has request limits (check API documentation)
- **Internet Required**: Script needs active internet connection
- **Logs**: Check `api_logs.txt` for troubleshooting
- **Currencies**: CoinGecko supports many currencies (usd, eur, gbp, etc.)

