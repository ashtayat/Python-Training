from country import CountryInfo
import requests
from PIL import Image
from io import BytesIO

def main():
    country_name = input("Enter the country name: ")
    
    country_info = CountryInfo()
    info = country_info.get_country_info(country_name)
    
    if info:
        print(f"Name: {info['name']}")
        print(f"Capital: {info['capital']}")
        print(f"Region: {info['region']}")
        print(f"Subregion: {info['subregion']}")
        print(f"Population: {info['population']}")
        print(f"Area: {info['area']} km²")
        print(f"Flag: {info['flag']}")

        # Display the flag image
        response = requests.get(info['flag'])
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.show()
        else:
            print("Failed to retrieve the flag image.")
    else:
        print("Country not found or API request failed.")


if __name__ == "__main__":
    main()