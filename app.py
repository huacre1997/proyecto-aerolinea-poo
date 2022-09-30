from model.Route import Route
from model.ScheduledFlight import ScheduledFlight
from typing import List, Dict
from config import CURRENCY_SYMBOL
import utils
# link typing: https://docs.python.org/3/library/typing.html?highlight=typing#module-typing


def create_list_routes() -> List[Route]:
    """
    Función que crea y devuelve una lista de objetos Route
    """
    data_routes: List[Dict[str, str | int | float]] = [
        {
            'code': 'LIM-AYA',
            'name': 'Lima - Ayacucho',
            'base_price_seat': 55.19,
            'price_economic_seat': 8,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 120,
            'economic_seats_max_sales': 130,
            'premium_seats_min_sales': 10,
            'premium_seats_max_sales': 20
        }, {
            'code': 'LIM-CUS',
            'name': 'Lima - Cusco',
            'base_price_seat': 136.51,
            'price_economic_seat': 8,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 130,
            'economic_seats_max_sales': 144,
            'premium_seats_min_sales': 15,
            'premium_seats_max_sales': 24
        }, {
            'code': 'LIM-ARE',
            'name': 'Lima - Arequipa',
            'base_price_seat': 90.29,
            'price_economic_seat': 8,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 115,
            'economic_seats_max_sales': 138,
            'premium_seats_min_sales': 16,
            'premium_seats_max_sales': 22
        }, {
            'code': 'LIM-TAR',
            'name': 'Lima - Tarapoto',
            'base_price_seat': 71.89,
            'price_economic_seat': 8,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 100,
            'economic_seats_max_sales': 120,
            'premium_seats_min_sales': 12,
            'premium_seats_max_sales': 18
        }, {
            'code': 'AYA-LIM',
            'name': 'Ayacucho - Lima',
            'base_price_seat': 40.42,
            'price_economic_seat': 7,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 100,
            'economic_seats_max_sales': 115,
            'premium_seats_min_sales': 10,
            'premium_seats_max_sales': 15
        }, {
            'code': 'CUS-LIM',
            'name': 'Cusco - Lima',
            'base_price_seat': 124.32,
            'price_economic_seat': 7,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 105,
            'economic_seats_max_sales': 120,
            'premium_seats_min_sales': 14,
            'premium_seats_max_sales': 20
        }, {
            'code': 'ARE-LIM',
            'name': 'Arequipa - Lima',
            'base_price_seat': 86.59,
            'price_economic_seat': 7,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 100,
            'economic_seats_max_sales': 110,
            'premium_seats_min_sales': 13,
            'premium_seats_max_sales': 18
        }, {
            'code': 'TAR-LIM',
            'name': 'Tarapoto - Lima',
            'base_price_seat': 68.42,
            'price_economic_seat': 7,
            'price_premium_seat': 16,
            'economic_seats_min_sales': 90,
            'economic_seats_max_sales': 105,
            'premium_seats_min_sales': 10,
            'premium_seats_max_sales': 15
        }
    ]

    # Lista de objetos Ruta
    routes: List[Route] = []

    # Iteramos la lista de Rutas.
    for key, route in enumerate(data_routes):
        # Creamos el objeto Ruta
        obj_route = Route(str(route['code']), str(route['name']), float(
            route['base_price_seat']), float(route['price_economic_seat']), float(route['price_premium_seat']), int(route['economic_seats_min_sales']), int(route['economic_seats_max_sales']), int(route['premium_seats_min_sales']), int(route['premium_seats_max_sales']))
        # Agregamos el objeto Route en una lista
        routes.append(obj_route)

    return routes


def create_list_flights(routes: List) -> List[ScheduledFlight]:
    """
    Función que crea y devuelve una lista de objetos Product
    """

    data_flights: List[Dict[str, str]] = [
        {
            'code': 'LIM-AYA',
            'airplane': 'A001'

        }, {
            'code': 'LIM-CUS',
            'airplane': 'A002'

        }, {
            'code': 'LIM-ARE',
            'airplane': 'A003'

        }, {
            'code': 'LIM-TAR',
            'airplane': 'A004'

        }, {
            'code': 'AYA-LIM',
            'airplane': 'A001'

        }, {
            'code': 'CUS-LIM',
            'airplane': 'A002'

        }, {
            'code': 'ARE-LIM',
            'airplane': 'A003'

        }, {
            'code': 'TAR-LIM',
            'airplane': 'A004'

        }
    ]

    # Creamos la lista de objetos ScheduledFlight
    flights: List[ScheduledFlight] = []

    for key, flight in enumerate(data_flights):
        # Buscamos nuestro objeto Ruta con el código de ruta del vuelo(flight)
        route = [r for r in routes if r.code == flight['code']]
        # Creamos nuestro objeto ScheduledFlight asignando la ruta encontrada [0] y el codigo del avión
        obj_product = ScheduledFlight(route[0], flight['airplane'])
        # Agregamos el objeto ScheduledFlight en una lista
        flights.append(obj_product)

    return flights


def main():
    """
    Función principal del módulo app.py
    """
    # Crear la lista de objetos de Rutas
    routes: List[Route] = create_list_routes()

    # Crear la lista de objetos de Vuelos programados
    flights: List[ScheduledFlight] = create_list_flights(routes)


if __name__ == "__main__":
    main()
