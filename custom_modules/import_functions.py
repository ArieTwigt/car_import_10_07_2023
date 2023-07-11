import requests
import sys


def import_car_brand(brand):
    print(f"Downloading cars for brand {brand}")

    # Convert the value of the brand to an uppercase
    selected_brand_upper = brand.upper()

    # Define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand_upper}"

    # Execute the request
    response = requests.get(endpoint)

    # Get the data from the response
    data = response.json()

    # Conditional statement that checks if the list with cars is not empty
    if len(data) == 0:
        print(f"No cars found for {brand}")
        sys.exit()

    return data