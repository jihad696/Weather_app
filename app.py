# app.py - Main Flask Application
from flask import Flask, render_template, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

print(f"DEBUG: OPENWEATHER_API_KEY = {OPENWEATHER_API_KEY}")

if not OPENWEATHER_API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY is not set! Please add it to your .env file.")

OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    """Render the main weather dashboard page"""
    return render_template('index.html')

@app.route('/api/weather/coords', methods=['POST'])
def get_weather_by_coords():
    """Get weather data by latitude and longitude"""
    try:
        data = request.get_json()
        lat = data.get('lat')
        lon = data.get('lon')
        
        if not lat or not lon:
            return jsonify({'error': 'Latitude and longitude are required'}), 400
        
        params = {
            'lat': lat,
            'lon': lon,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(OPENWEATHER_BASE_URL, params=params, timeout=10)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch weather data'}), response.status_code
            
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timeout. Please try again.'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Network error. Please check your connection.'}), 503
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.route('/api/weather/city', methods=['POST'])
def get_weather_by_city():
    """Get weather data by city name"""
    try:
        data = request.get_json()
        city = data.get('city')
        
        if not city:
            return jsonify({'error': 'City name is required'}), 400
        
        params = {
            'q': city,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(OPENWEATHER_BASE_URL, params=params, timeout=10)
        
        if response.status_code == 200:
            return jsonify(response.json())
        elif response.status_code == 404:
            return jsonify({'error': 'City not found. Please check the spelling.'}), 404
        else:
            return jsonify({'error': 'Failed to fetch weather data'}), response.status_code
            
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timeout. Please try again.'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Network error. Please check your connection.'}), 503
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)