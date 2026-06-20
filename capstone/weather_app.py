def mock_weather_app(city):
    mock_data = {"London": "15C, Rainy", "New York": "20C, Sunny"}
    return mock_data.get(city, "Data not available")
