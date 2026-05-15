import os
import dotenv
import requests
import rich
import rich.table
import rich.panel
import rich.box
import rich.console

# Create console object for managing console
console = rich.console.Console()

def display_weather(data, city_name):
    if not data:
        return

    # Extract data
    temperature_c = data["current"]["temperature"]
    temperature_f = round(data["current"]["temperature"] * 1.8 + 32, 2)
    description = data["current"]["weather_descriptions"][0]
    feels_like = data["current"]["feelslike"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_speed"]

    # Create a table for the data
    table = rich.table.Table(show_header=False, box=rich.box.ROUNDED, border_style="cyan")

    table.add_row("[bold yellow]Condition:[/]", f"[white]{description}[/]")
    table.add_row("[bold yellow]Temperature:[/]", f"[bold magenta]{temperature_c}°C[/] ({temperature_f:.1f}°F)")
    table.add_row("[bold yellow]Feels like:[/]", f"{feels_like}°C")
    table.add_row("[bold yellow]Wind speed:[/]", f"{wind_speed} km/h")
    table.add_row("[bold yellow]Humidity:[/]", f"{humidity}%")

    panel = rich.panel.Panel(
        table,
        title=f"[bold green]Weather report: {city_name.capitalize()}[/]",
        subtitle="[italic blue]Data provided by WeatherStack[/]",
        expand=False
    )

    console.print(panel)

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
        if info:
            display_weather(info, city)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # This block will execute when pressed Ctrl+C or close the program
        print("\nProgram closed by user. Goodbye!")
    except EOFError:
        # This block will execute when pressed Ctrl+D
        print("\nInput interrupted. Exiting...")