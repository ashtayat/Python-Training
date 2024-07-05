# Final Project 
Project Overview
This project fetches and displays information about a country using the REST Countries API. 
It applies basic Object-Oriented Programming (OOP) principles and displays the country's flag using the Pillow library.

# Project Structure
country_info_app/
country.py: Contains the CountryInfo class that handles API interaction.
main.py: The main script that interacts with the user, fetches country information, and displays it.
requirements.txt: Lists the dependencies required for the project.

# country.py
This file defines the CountryInfo class, which is responsible for interacting with the REST Countries API.

# Key Points:
__init__ Method: Initializes the CountryInfo object with the base URL for the REST Countries API.
get_country_info Method:
Constructs the full API URL using the base URL and the country name.
Sends a GET request to the API.
If the request is successful (status_code is 200), it parses the JSON response to extract the country's information.
Returns a dictionary containing the country's name, capital, region, subregion, population, area, and flag URL.
If the request fails, it returns None.

# main.py
This file contains the main script that uses the CountryInfo class to fetch and display information about a country.
# Key Points:
Imports:
CountryInfo class from country.py.
requests for making HTTP requests.
Pillow library's Image class for displaying images.
BytesIO for handling byte data.

# main Function:
Prompts the user to enter a country name.
Creates an instance of the CountryInfo class.
Calls the get_country_info method to fetch information about the specified country.
If the information is successfully fetched:
Prints the country's name, capital, region, subregion, population, area, and flag URL.
Sends a GET request to fetch the flag image.
If the flag image request is successful, it displays the image using Pillow.
If the information is not fetched successfully, it prints an error message.
Entry Point:

if __name__ == "__main__": main() ensures that the main function is called when the script is run directly.

# requirements.txt
This file lists the dependencies required for the project.