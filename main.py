import requests

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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # This block will execute when pressed Ctrl+C or close the program
        print("\nProgram closed by user. Goodbye!")
    except EOFError:
        # This block will execute when pressed Ctrl+D
        print("\nInput interrupted. Exiting...")