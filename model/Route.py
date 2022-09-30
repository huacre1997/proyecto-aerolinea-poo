import random
# link random: https://docs.python.org/3/library/random.html


class Route(object):
    def __init__(self, code: str, name: str, base_price_seat: float,
                 price_economic_seat: float, price_premium_seat: float,
                 economic_seats_min_sales: int, economic_seats_max_sales: int,
                 premium_seats_min_sales: int, premium_seats_max_sales: int):
        """
        Constructor de la Clase Route
        """
        self.code: str = code
        self.name: str = name
        self.base_price_seat: float = base_price_seat
        self.price_economic_seat: float = price_economic_seat
        self.price_premium_seat: float = price_premium_seat
        self.economic_seats_min_sales: int = economic_seats_min_sales
        self.economic_seats_max_sales: int = economic_seats_max_sales
        self.premium_seats_min_sales: int = premium_seats_min_sales
        self.premium_seats_max_sales: int = premium_seats_max_sales

    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.name

    def get_rand_premium_ticket_sales(self) -> int:
        """
        Devuelve un número de tickets de manera aleatoria basada en el rango
        de ventas mínimas y máximas de la ruta.
        """
        return random.randint(self.premium_seats_min_sales, self.premium_seats_max_sales)

    def get_rand_economic_ticket_sales(self) -> int:
        """
        Devuelve un número de tickets de manera aleatoria basada en el rango
        de ventas mínimas y máximas de la ruta.
        """
        return random.randint(self.economic_seats_min_sales, self.economic_seats_max_sales)
