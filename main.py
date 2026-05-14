import os

import requests
import os
import dotenv

# Load environment variables from the .env file
dotenv.load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city_name):
    if not API_KEY:
        print("Error: API Key not found in .env file!")
        return None

    # Build the request URL
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city_name}"

    try:
        # Use the requests module directly to send an HTTP GET request
        response = requests.get(url)
        # Convert the response from JSON format into a Python dictionary
        data = response.json()

        # Check if the API returned an error message
        if "error" in data:
            print(f"API Error: {data['error']['info']}")
            return None

        return data

    except Exception as e:
        print(f"Network error: {e}")
        return None

def main():
    print("--- Welcome to Weather application! ---")

    while True:
        # Asking user to enter the city
        city = input("Enter city/postal code (or 'exit' for quit): ").strip()

        # Exit condition for the program
        if city.lower() == "exit":
            print("Goodbye. See you again soon")
            break
        # Check for empty input
        if not city:
            print("Error: city or postal code required")
            continue

        info = get_weather(city)
        print (info)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # This block will execute when pressed Ctrl+C or close the program
        print("\nProgram closed by user. Goodbye!")
    except EOFError:
        # This block will execute when pressed Ctrl+D
        print("\nInput interrupted. Exiting...")