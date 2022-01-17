# weather.py
import requests, pprint


class Weather:
    """Create a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # Get your own api key from https://openweathermap.org

    # Examples:
    weather = Weather(apikey, city="Madrid")
    print(weather.next_12h())

    weather = Weather(apikey, lat=4.1, lon=4.5)
    pprint.pprint(weather.next_12h())

    weather = Weather(apikey, lat=4.1, lon=4.5)
    pprint.pprint(weather.next_12h_simplified())


    """

    def __init__(self, api, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api}&units=imperial"
            r = requests.get(url)
            self.data = r.json()  # to see the dictionary data
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={api}&units=imperial"
            r = requests.get(url)
            self.data = r.json()  # to see the dictionary data
        else:
            raise TypeError("Provide either a city or lat and lon arguments")

        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a dict
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """Returns data, temperature, and sky conditions every 3 hours
        for the next 12 hours as a tuple of tuples.
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'],
                               dicty['main']['temp'],
                               dicty['weather'][0]['description']))
        return simple_data


if __name__ == "__main__":

    apikey = "6f33f9b058812fbb61be38c571a0d0a0"

    print("By city:")
    weather = Weather(apikey, city="Madrid")
    print(weather.next_12h())

    print("By lat and lon")
    weather = Weather(apikey, lat=4.1, lon=4.5)
    pprint.pprint(weather.next_12h())

    print("By lat and lon simplified")
    weather = Weather(apikey, lat=4.1, lon=4.5)
    pprint.pprint(weather.next_12h_simplified())
