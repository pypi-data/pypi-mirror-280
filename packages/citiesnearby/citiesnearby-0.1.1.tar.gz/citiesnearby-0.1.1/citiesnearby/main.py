import requests



class CitiesNearby:
    def __init__(self, token):
        self.token = token
        self._base_url = 'http://api.marz1kcheck.pp.ua'

    def get_cities_by_name(self, city: str, radius: int = 30, limit: int = 10) -> dict:
        """
        Returning all cities in X radius from the given city.

        :param city: City name
        :param radius: Radius of search. Start point of the radius is the given city. Min=1, Max=100.
        :param limit: Limit of the cities to return. Min=1, Max=100.
        :return: Dict with all the cities with their name, country, coordinates, population, distance to the center.
        """

        response = requests.get(self._base_url+f'/getCitiesByName?name={city}&radius={radius}&limit={limit}',
                                headers={'X-Token': self.token})
        return response.json()

    def get_cities_by_coordinates(self, lat: float, lng: float, radius: int = 30, limit: int = 10) -> dict:
        """
        Returning all cities in X radius from the given coordinates.

        :param lat: Latitude of the start point.
        :param lng: Longitude of the start point.
        :param radius: Radius of search. Start point of the radius is the given coordinates. Min=1, Max=100.
        :param limit: Limit of the cities to return. Min=1, Max=100.
        :return: Dict with all the cities with their name, country, coordinates, population, distance to the center.
        """

        response = requests.get(self._base_url + f'/getCitiesByCoord?lat={lat}&lng={lng}&radius={radius}&limit={limit}',
                                headers={'X-Token': self.token})
        return response.json()

    def get_cities_by_ip(self, ip: str, radius: int = 30, limit: int = 10) -> dict:
        """
        Returning all cities in X radius from the given coordinates.

        :param ip: IP address
        :param radius: Radius of search. Start point of the radius is the given IP. Min=1, Max=100.
        :param limit: Limit of the cities to return. Min=1, Max=100.
        :return: Dict with all the cities with their name, country, coordinates, population, distance to the center.
        """
        response = requests.get(self._base_url + f'/getCitiesByIP?ip={ip}&radius={radius}&limit={limit}',
                                headers={'X-Token': self.token})
        return response.json()