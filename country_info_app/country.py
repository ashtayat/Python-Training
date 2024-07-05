import requests

class CountryInfo:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1/name/"

    def get_country_info(self, country_name):
        url = f"{self.base_url}{country_name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()[0]  # Get the first result
            return {
                'name': data.get('name', {}).get('common', 'N/A'),
                'capital': data.get('capital', ['N/A'])[0],
                'region': data.get('region', 'N/A'),
                'subregion': data.get('subregion', 'N/A'),
                'population': data.get('population', 'N/A'),
                'area': data.get('area', 'N/A'),
                'flag': data.get('flags', {}).get('png', 'N/A')
            }
        else:
            return None
