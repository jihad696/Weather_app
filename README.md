# Weather App

A modern, responsive weather dashboard application built with Flask and OpenWeather API. Get real-time weather information by city name or geolocation with an intuitive, visually appealing interface.

## Features

- **City Search**: Search weather by city name
- **Geolocation**: Fetch weather data based on your current location
- **Real-time Data**: Current temperature, conditions, humidity, and more
- **Dynamic Backgrounds**: Background changes based on weather conditions
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Error Handling**: Comprehensive error handling for network and API issues
- **Clean UI**: Modern, glassmorphic design with smooth animations

## Prerequisites

- Python 3.8 or higher
- An OpenWeather API key (free tier available at [openweathermap.org](https://openweathermap.org/api))

## Installation

### 1. Clone or Download the Project

```bash
cd /path/to/Weather_app
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenWeather API key.

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Project Structure

```
Weather_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in repo)
└── templates/
    └── index.html         # Frontend UI
```

## API Endpoints

### GET `/`
Renders the main weather dashboard page.

**Response**: HTML page

---

### POST `/api/weather/city`
Fetch weather data by city name.

**Request Body**:
```json
{
  "city": "London"
}
```

**Response (Success - 200)**:
```json
{
  "coord": { "lon": -0.1257, "lat": 51.5085 },
  "weather": [{ "id": 500, "main": "Rain", "description": "light rain" }],
  "main": {
    "temp": 10.5,
    "feels_like": 9.2,
    "humidity": 80,
    "pressure": 1013
  },
  "wind": { "speed": 5.2 },
  "clouds": { "all": 90 },
  "sys": { "country": "GB", "sunrise": 1641638400, "sunset": 1641671100 },
  "name": "London",
  "timezone": 0
}
```

**Response (Error - 404)**:
```json
{
  "error": "City not found. Please check the spelling."
}
```

**Status Codes**:
- `200`: Success
- `400`: Missing city name
- `404`: City not found
- `504`: Request timeout
- `503`: Network error

---

### POST `/api/weather/coords`
Fetch weather data by latitude and longitude.

**Request Body**:
```json
{
  "lat": 51.5085,
  "lon": -0.1257
}
```

**Response (Success - 200)**: Same as `/api/weather/city`

**Response (Error - 400)**:
```json
{
  "error": "Latitude and longitude are required"
}
```

**Status Codes**:
- `200`: Success
- `400`: Missing coordinates
- `504`: Request timeout
- `503`: Network error
- `500`: Unexpected error

---

## Dependencies

- **Flask** (3.1.0): Lightweight web framework
- **requests** (2.32.3): HTTP library for API calls
- **python-dotenv** (1.0.1): Environment variable management
- **Werkzeug** (3.1.3): WSGI utilities

## Frontend Features

### Search Functionality
- Enter a city name to fetch weather data
- Click "Search" button or press Enter to submit
- Results display current weather conditions

### Geolocation
- Click "Use My Location" to fetch weather for your current coordinates
- Browser will request permission to access your location
- Automatically fetches weather upon location access

### Dynamic UI
- Background color changes based on weather conditions:
  - ☀️ **Clear**: Orange/red gradient
  - ☁️ **Clouds**: Gray/dark gradient
  - 🌧️ **Rain**: Blue gradient
  - ❄️ **Snow**: Light blue gradient

### Error Handling
- User-friendly error messages for:
  - Missing city names
  - City not found
  - Network errors
  - Timeout errors

## Environment Variables

Create a `.env` file with the following variables:

```
OPENWEATHER_API_KEY=your_openweather_api_key
```

### Getting an API Key

1. Visit [openweathermap.org](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key from your account dashboard
4. Add it to the `.env` file

## Configuration

Default server configuration in `app.py`:
- **Host**: 127.0.0.1 (localhost)
- **Port**: 5000
- **Debug Mode**: Enabled

To change these, modify the last line of `app.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5000)
```

## Troubleshooting

### "OPENWEATHER_API_KEY is not set"
- Ensure `.env` file exists in the project root
- Verify the API key is correctly set
- Restart the application

### "City not found"
- Check the spelling of the city name
- Try using city names with country codes (e.g., "London, GB")

### "Request timeout"
- Check your internet connection
- The OpenWeather API may be experiencing issues
- Try again in a few moments

### Geolocation not working
- Ensure you granted browser permission to access location
- Some browsers block geolocation for non-HTTPS sites in production
- Try using the search feature instead

## Customization

### Change Server Port
Edit the last line in `app.py`:
```python
app.run(debug=True, host='127.0.0.1', port=8000)  # Change 5000 to 8000
```

### Modify Units (Fahrenheit vs Celsius)
In `app.py`, change the `units` parameter in the API requests:
```python
'units': 'imperial'  # For Fahrenheit
'units': 'metric'    # For Celsius (default)
```

### Customize Colors and Styling
Edit the CSS in `templates/index.html` under the `<style>` tag

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your OpenWeather API key is valid
3. Ensure all dependencies are correctly installed
4. Check your internet connection

## Author

Created as part of Nagwa Tasks

## Acknowledgments

- Weather data provided by [OpenWeather](https://openweathermap.org/)
- Built with Flask and vanilla JavaScript
