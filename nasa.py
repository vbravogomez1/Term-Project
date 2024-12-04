# Used shell from MBTA-Web-App-Project for this project

import os
import json
import urllib.request
import pprint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
NASA_API_KEY = os.getenv("NASA_API_KEY")

# Useful base URL for the NASA API
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"

def get_json(url: str) -> dict:
    """
    given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.
    
    this function will be used to fetch the astronomy picture of the day based on a specific date.
    """
    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode("utf-8")
        data = json.loads(response_text)
        pprint.pprint(data)
    return data

def get_apod(date: str) -> dict:
    """
    return the Astronomy Picture of the Day based on the provided date.

    we used ChatGPT to debug and figure out why our code wasn't working initially. 
    """
    url = f"{NASA_APOD_URL}?api_key={NASA_API_KEY}&date={date}"
    return get_json(url)

def main():
    """
    Had to use ChatGPT for this part as our program was not running correctly, we were not getting the HTML link
    
    Main function to test the NASA APOD API connectivity and response parsing.
    """
    print("Testing NASA APOD API")
    date = "2023-10-01"  # Use a specific date for testing
    apod_data = get_apod(date)
    print("API Test Completed: \n", apod_data)

if __name__ == "__main__":
    main()
    