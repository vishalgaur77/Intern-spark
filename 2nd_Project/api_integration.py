# ==========================================
# API INTEGRATION PROJECT
# Weather / Crypto / News APIs
# ==========================================

import requests
import json
from datetime import datetime
from typing import Dict, List, Optional

# ==========================================
# CONFIGURATION
# ==========================================

# Free API Keys and Endpoints (Public/Freemium)
WEATHER_API_KEY = "demo"  # Get from openweathermap.org
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

CRYPTO_API_URL = "https://api.coingecko.com/api/v3"  # No key needed (Free)

NEWS_API_KEY = "demo"  # Get from newsapi.org
NEWS_API_URL = "https://newsapi.org/v2"

# ==========================================
# ERROR HANDLING & LOGGING
# ==========================================

def log_api_call(api_name: str, status: str, message: str = ""):
    """
    Logs API calls with timestamp
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {api_name} - {status}"
    if message:
        log_message += f" - {message}"
    
    with open("api_logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")
    
    return log_message


def handle_api_error(response: requests.Response, api_name: str) -> Optional[Dict]:
    """
    Handles API errors and exceptions
    """
    try:
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            error_msg = f"{api_name}: Resource not found (404)"
            print(f"❌ {error_msg}")
            log_api_call(api_name, "ERROR", error_msg)
            return None
        elif response.status_code == 401:
            error_msg = f"{api_name}: Invalid API key (401)"
            print(f"❌ {error_msg}")
            log_api_call(api_name, "ERROR", error_msg)
            return None
        elif response.status_code == 429:
            error_msg = f"{api_name}: Rate limit exceeded (429)"
            print(f"❌ {error_msg}")
            log_api_call(api_name, "ERROR", error_msg)
            return None
        else:
            error_msg = f"{api_name}: HTTP {response.status_code}"
            print(f"❌ {error_msg}")
            log_api_call(api_name, "ERROR", error_msg)
            return None
    except Exception as e:
        error_msg = f"{api_name}: {str(e)}"
        print(f"❌ {error_msg}")
        log_api_call(api_name, "ERROR", error_msg)
        return None


# ==========================================
# WEATHER API INTEGRATION
# ==========================================

def fetch_weather(city: str, units: str = "metric") -> Optional[Dict]:
    """
    Fetches weather data for a city
    units: 'metric' (Celsius), 'imperial' (Fahrenheit)
    """
    try:
        print(f"\n🌍 Fetching weather for {city}...")
        
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": units
        }
        
        response = requests.get(WEATHER_API_URL, params=params, timeout=5)
        data = handle_api_error(response, "Weather API")
        
        if data:
            log_api_call("Weather API", "SUCCESS", f"City: {city}")
        
        return data
    
    except requests.exceptions.Timeout:
        print("❌ Weather API: Request timeout")
        log_api_call("Weather API", "ERROR", "Request timeout")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Weather API: Connection error")
        log_api_call("Weather API", "ERROR", "Connection error")
        return None
    except Exception as e:
        print(f"❌ Weather API: {str(e)}")
        log_api_call("Weather API", "ERROR", str(e))
        return None


def display_weather(data: Dict, units: str = "metric"):
    """
    Displays weather data in readable format
    """
    try:
        print("\n" + "=" * 50)
        print("🌤️  WEATHER INFORMATION")
        print("=" * 50)
        
        city = data.get("name", "N/A")
        country = data.get("sys", {}).get("country", "N/A")
        temp = data.get("main", {}).get("temp", "N/A")
        feels_like = data.get("main", {}).get("feels_like", "N/A")
        humidity = data.get("main", {}).get("humidity", "N/A")
        pressure = data.get("main", {}).get("pressure", "N/A")
        description = data.get("weather", [{}])[0].get("description", "N/A")
        wind_speed = data.get("wind", {}).get("speed", "N/A")
        
        unit_symbol = "°C" if units == "metric" else "°F"
        
        print(f"\n📍 Location: {city}, {country}")
        print(f"🌡️  Temperature: {temp}{unit_symbol} (feels like {feels_like}{unit_symbol})")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌪️  Wind Speed: {wind_speed} m/s")
        print(f"⚡ Pressure: {pressure} hPa")
        print(f"📝 Condition: {description.capitalize()}")
        
        print("\n" + "=" * 50)
        
    except Exception as e:
        print(f"❌ Error displaying weather: {str(e)}")


# ==========================================
# CRYPTO API INTEGRATION
# ==========================================

def fetch_crypto_prices(crypto_ids: List[str] = None, currency: str = "usd") -> Optional[Dict]:
    """
    Fetches cryptocurrency prices
    crypto_ids: List of crypto IDs (bitcoin, ethereum, cardano, etc.)
    currency: usd, eur, gbp, etc.
    """
    try:
        if crypto_ids is None:
            crypto_ids = ["bitcoin", "ethereum", "cardano", "solana", "ripple"]
        
        print(f"\n💰 Fetching crypto prices for: {', '.join(crypto_ids)}...")
        
        url = f"{CRYPTO_API_URL}/simple/price"
        params = {
            "ids": ",".join(crypto_ids),
            "vs_currencies": currency,
            "include_market_cap": "true",
            "include_24hr_vol": "true",
            "include_24hr_change": "true"
        }
        
        response = requests.get(url, params=params, timeout=5)
        data = handle_api_error(response, "Crypto API")
        
        if data:
            log_api_call("Crypto API", "SUCCESS", f"Fetched {len(data)} cryptocurrencies")
        
        return data
    
    except requests.exceptions.Timeout:
        print("❌ Crypto API: Request timeout")
        log_api_call("Crypto API", "ERROR", "Request timeout")
        return None
    except Exception as e:
        print(f"❌ Crypto API: {str(e)}")
        log_api_call("Crypto API", "ERROR", str(e))
        return None


def filter_crypto_by_price(data: Dict, min_price: float = 0, max_price: float = float('inf'), currency: str = "usd") -> Dict:
    """
    Filters cryptocurrency by price range
    """
    filtered = {}
    
    for crypto, prices in data.items():
        price = prices.get(currency, 0)
        if min_price <= price <= max_price:
            filtered[crypto] = prices
    
    return filtered


def display_crypto(data: Dict, currency: str = "usd"):
    """
    Displays cryptocurrency data in readable format
    """
    try:
        print("\n" + "=" * 80)
        print(f"💰 CRYPTOCURRENCY PRICES ({currency.upper()})")
        print("=" * 80)
        print(f"{'Cryptocurrency':<20} {'Price':<15} {'Market Cap':<20} {'24h Change':<15}")
        print("-" * 80)
        
        for crypto, prices in data.items():
            price = prices.get(currency, "N/A")
            market_cap = prices.get(f"{currency}_market_cap", "N/A")
            change_24h = prices.get(f"{currency}_24h_change", "N/A")
            
            # Format values
            price_str = f"{currency.upper()} {price:,.2f}" if isinstance(price, (int, float)) else str(price)
            market_cap_str = f"{currency.upper()} {market_cap:,.0f}" if isinstance(market_cap, (int, float)) else str(market_cap)
            change_str = f"{change_24h:.2f}%" if isinstance(change_24h, (int, float)) else str(change_24h)
            
            # Color coding for 24h change
            if isinstance(change_24h, (int, float)):
                change_indicator = "📈" if change_24h > 0 else "📉"
                change_str = f"{change_indicator} {change_str}"
            
            print(f"{crypto.capitalize():<20} {price_str:<15} {market_cap_str:<20} {change_str:<15}")
        
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Error displaying crypto: {str(e)}")


# ==========================================
# NEWS API INTEGRATION
# ==========================================

def fetch_news(query: str = None, category: str = "general", country: str = "us", 
               sort_by: str = "publishedAt", page: int = 1) -> Optional[Dict]:
    """
    Fetches news articles
    query: Search term
    category: business, entertainment, general, health, science, sports, technology
    country: ISO country code (us, gb, in, etc.)
    sort_by: publishedAt, relevancy, popularity
    """
    try:
        if query:
            print(f"\n📰 Searching news for: {query}...")
            url = f"{NEWS_API_URL}/everything"
            params = {
                "q": query,
                "sortBy": sort_by,
                "page": page,
                "pageSize": 10,
                "apiKey": NEWS_API_KEY
            }
        else:
            print(f"\n📰 Fetching {category} news...")
            url = f"{NEWS_API_URL}/top-headlines"
            params = {
                "category": category,
                "country": country,
                "page": page,
                "pageSize": 10,
                "apiKey": NEWS_API_KEY
            }
        
        response = requests.get(url, params=params, timeout=5)
        data = handle_api_error(response, "News API")
        
        if data:
            total_results = data.get("totalResults", 0)
            log_api_call("News API", "SUCCESS", f"Found {total_results} articles")
        
        return data
    
    except requests.exceptions.Timeout:
        print("❌ News API: Request timeout")
        log_api_call("News API", "ERROR", "Request timeout")
        return None
    except Exception as e:
        print(f"❌ News API: {str(e)}")
        log_api_call("News API", "ERROR", str(e))
        return None


def filter_news_by_source(articles: List[Dict], source_name: str) -> List[Dict]:
    """
    Filters news articles by source
    """
    return [article for article in articles if article.get("source", {}).get("name", "").lower() == source_name.lower()]


def filter_news_by_keyword(articles: List[Dict], keyword: str) -> List[Dict]:
    """
    Filters news articles by keyword in title or description
    """
    keyword = keyword.lower()
    return [article for article in articles 
            if keyword in article.get("title", "").lower() or 
               keyword in article.get("description", "").lower()]


def display_news(data: Dict, max_articles: int = 5):
    """
    Displays news articles in readable format
    """
    try:
        articles = data.get("articles", [])
        total_results = data.get("totalResults", 0)
        
        print("\n" + "=" * 100)
        print(f"📰 NEWS ARTICLES (Showing {min(max_articles, len(articles))} of {total_results})")
        print("=" * 100)
        
        for idx, article in enumerate(articles[:max_articles], 1):
            source = article.get("source", {}).get("name", "Unknown")
            title = article.get("title", "No title")
            description = article.get("description", "No description")
            url = article.get("url", "No URL")
            published_at = article.get("publishedAt", "Unknown")
            
            # Format published date
            try:
                date_obj = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                published_at = date_obj.strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass
            
            print(f"\n📌 Article {idx}")
            print(f"   📢 Source: {source}")
            print(f"   📝 Title: {title}")
            print(f"   📄 Description: {description[:150]}..." if len(description) > 150 else f"   📄 Description: {description}")
            print(f"   🔗 URL: {url}")
            print(f"   ⏰ Published: {published_at}")
            print("-" * 100)
        
        print("=" * 100)
        
    except Exception as e:
        print(f"❌ Error displaying news: {str(e)}")


# ==========================================
# MAIN MENU & USER INTERFACE
# ==========================================

def display_main_menu():
    """
    Displays main menu options
    """
    print("\n" + "=" * 50)
    print("🌐 API INTEGRATION PROJECT")
    print("=" * 50)
    print("\n📋 Choose an API:")
    print("  1. 🌍 Weather API")
    print("  2. 💰 Crypto API")
    print("  3. 📰 News API")
    print("  4. ❓ Get API Information")
    print("  5. 🚪 Exit")
    print("=" * 50)


def display_weather_submenu():
    """
    Displays weather API options
    """
    print("\n" + "=" * 50)
    print("🌍 WEATHER API MENU")
    print("=" * 50)
    print("\n🔧 Choose an option:")
    print("  1. Get weather by city")
    print("  2. Get weather in Celsius")
    print("  3. Get weather in Fahrenheit")
    print("  4. Back to main menu")
    print("=" * 50)


def display_crypto_submenu():
    """
    Displays crypto API options
    """
    print("\n" + "=" * 50)
    print("💰 CRYPTO API MENU")
    print("=" * 50)
    print("\n🔧 Choose an option:")
    print("  1. Get top 5 cryptocurrencies")
    print("  2. Search specific cryptocurrencies")
    print("  3. Filter by price range")
    print("  4. Back to main menu")
    print("=" * 50)


def display_news_submenu():
    """
    Displays news API options
    """
    print("\n" + "=" * 50)
    print("📰 NEWS API MENU")
    print("=" * 50)
    print("\n🔧 Choose an option:")
    print("  1. Top headlines by category")
    print("  2. Search news by keyword")
    print("  3. Filter by source")
    print("  4. Back to main menu")
    print("=" * 50)


def get_api_info():
    """
    Displays information about APIs
    """
    print("\n" + "=" * 80)
    print("ℹ️  API INFORMATION")
    print("=" * 80)
    
    print("\n🌍 WEATHER API (OpenWeatherMap)")
    print("-" * 80)
    print("  Website: https://openweathermap.org/api")
    print("  Features: Real-time weather, forecasts, historical data")
    print("  Free Tier: Up to 1000 calls/day")
    print("  Setup: Get free API key from openweathermap.org")
    print("  Parameters: City, Country code, Units (metric/imperial)")
    
    print("\n💰 CRYPTO API (CoinGecko)")
    print("-" * 80)
    print("  Website: https://www.coingecko.com/api")
    print("  Features: Cryptocurrency prices, market data, historical data")
    print("  Free Tier: Unlimited requests (public)")
    print("  Setup: No API key required!")
    print("  Parameters: Crypto IDs, Currency, Time period")
    
    print("\n📰 NEWS API (NewsAPI)")
    print("-" * 80)
    print("  Website: https://newsapi.org")
    print("  Features: Top headlines, search articles, filters by category")
    print("  Free Tier: Up to 100 requests/day")
    print("  Setup: Get free API key from newsapi.org")
    print("  Parameters: Keywords, Category, Country, Sort order")
    
    print("\n" + "=" * 80)


def weather_operations():
    """
    Weather API operations
    """
    while True:
        display_weather_submenu()
        choice = input("\n👉 Enter your choice (1-4): ").strip()
        
        if choice == "1" or choice == "2" or choice == "3":
            city = input("🏙️  Enter city name: ").strip()
            if not city:
                print("❌ Invalid city name!")
                continue
            
            units = "metric" if choice == "2" else ("imperial" if choice == "3" else "metric")
            data = fetch_weather(city, units)
            
            if data:
                display_weather(data, units)
        
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.")


def crypto_operations():
    """
    Crypto API operations
    """
    while True:
        display_crypto_submenu()
        choice = input("\n👉 Enter your choice (1-4): ").strip()
        
        if choice == "1":
            data = fetch_crypto_prices()
            if data:
                display_crypto(data)
        
        elif choice == "2":
            cryptos_input = input("🔍 Enter crypto IDs (comma-separated, e.g., bitcoin,ethereum,ripple): ").strip()
            if cryptos_input:
                cryptos = [c.strip().lower() for c in cryptos_input.split(",")]
                data = fetch_crypto_prices(cryptos)
                if data:
                    display_crypto(data)
        
        elif choice == "3":
            try:
                data = fetch_crypto_prices()
                if data:
                    min_price = float(input("💵 Enter minimum price: ").strip())
                    max_price = float(input("💵 Enter maximum price: ").strip())
                    filtered = filter_crypto_by_price(data, min_price, max_price)
                    if filtered:
                        display_crypto(filtered)
                    else:
                        print("❌ No cryptocurrencies found in that price range!")
            except ValueError:
                print("❌ Invalid price input!")
        
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.")


def news_operations():
    """
    News API operations
    """
    while True:
        display_news_submenu()
        choice = input("\n👉 Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n📂 Categories: business, entertainment, general, health, science, sports, technology")
            category = input("📂 Enter category (default: general): ").strip().lower() or "general"
            data = fetch_news(category=category)
            if data:
                display_news(data)
        
        elif choice == "2":
            query = input("🔍 Enter search keyword: ").strip()
            if query:
                data = fetch_news(query=query)
                if data:
                    display_news(data)
            else:
                print("❌ Invalid search query!")
        
        elif choice == "3":
            articles_data = fetch_news()
            if articles_data:
                articles = articles_data.get("articles", [])
                source_name = input("🏢 Enter source name to filter: ").strip()
                filtered = filter_news_by_source(articles, source_name)
                
                if filtered:
                    filtered_data = articles_data.copy()
                    filtered_data["articles"] = filtered
                    display_news(filtered_data, max_articles=len(filtered))
                else:
                    print(f"❌ No articles found from source: {source_name}")
        
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.")


def main():
    """
    Main program loop
    """
    try:
        log_api_call("SYSTEM", "START", "API Integration program started")
        print("\n✅ Program initialized. Logs will be saved to api_logs.txt")
        
        while True:
            display_main_menu()
            choice = input("\n👉 Enter your choice (1-5): ").strip()
            
            if choice == "1":
                weather_operations()
            elif choice == "2":
                crypto_operations()
            elif choice == "3":
                news_operations()
            elif choice == "4":
                get_api_info()
            elif choice == "5":
                print("\n✅ Thank you for using API Integration!")
                log_api_call("SYSTEM", "END", "API Integration program ended")
                break
            else:
                print("❌ Invalid choice! Please enter 1-5.")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Program interrupted by user!")
        log_api_call("SYSTEM", "INTERRUPT", "User interrupted program")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        log_api_call("SYSTEM", "ERROR", str(e))


if __name__ == "__main__":
    main()
