# 🌦️ Terminal Weather App

A stylish Python command-line application that fetches real-time weather data using the **WeatherStack API**. Built with a focus on clean UI.

---

## ✨ Features
* **Live Weather Data:** Real-time updates for any city or postal code worldwide.
* **Modern UI:** Beautifully formatted tables and panels thanks to the `Rich` library.
* **Smart Conversions:** Automatically calculates temperatures in both Celsius and Fahrenheit (following Tony Gaddis' logic).
* **Error Handling:** Robust protection against network issues, invalid API keys, and empty inputs.

---

## 🛠️ Tech Stack
* **Python 3.10+**
* **Libraries:** `requests`, `python-dotenv`, `rich`
* **API:** [WeatherStack](https://weatherstack.com/)
* **OS:** Optimized for Ubuntu/Linux terminals.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/titovmas/weather-app.git
   cd weather-app
   ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configuration & Environment Setup**
    This application follows industry best practices by separating configuration from the source code using environment variables.

    #### Creating the Environment File
    
    The program is designed to automatically detect and load credentials from a file named .env located in the project's root directory.

    To set up your environment:

    Create the `.env` file:

    ```bash
    touch .env
    ```
    Define your API key by adding the following line to the file:
    ```env
    WEATHER_API_KEY=your_access_key_here
    ```
    
    #### Security & Version Control
    In a standard development workflow, the `.env` file is strictly private. It should be added to your `.gitignore` to prevent sensitive information from being leaked to version control systems.

    Note: For evaluation purposes, a pre-configured `.env` file may be included in this repository to ensure the application is "ready-to-run" immediately upon download. For long-term use, please replace it with your personal key from WeatherStack.

## 🏃 Running the App
After configuration, simply run:

    ```bash
    python3 main.py
    ```
