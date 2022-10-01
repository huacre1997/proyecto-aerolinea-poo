from config import IGV_TOTAL
from model.Route import Route
from typing import List

# map() => aplica una función a todos los elementos en un dato iterable (listas,tuplas,diccionarios).
# link: https://docs.python.org/3/library/functions.html#map


class ScheduledFlight(object):
    def __init__(self, route: Route, airplane):
        """
        Constructor de la Clase ScheduledFlight
        """
        self.route: Route = route
        self.airplane: str = airplane
        self.generate_economic_tickets()
        self.generate_premium_tickets()

    def generate_economic_tickets(self) -> None:
        """
        Genera un listado de tickets económicos y lo asigna como atributo de la clase
        """
        tickets: int = self.route.get_rand_economic_ticket_sales()
        list_tickets_economic: list = []
        for i in range(tickets):
            economic_ticket_cost: float = (
                float(self.route.base_price_seat) + float(self.route.price_economic_seat))
            list_tickets_economic.append(economic_ticket_cost)
        self.economic_sold_tickets: List = list_tickets_economic

    def generate_premium_tickets(self) -> None:
        """
        Genera un listado de tickets premium y lo asigna como atributo de la clase
        """
        tickets: int = self.route.get_rand_premium_ticket_sales()
        list_tickets: list = []
        for i in range(tickets):
            premium_ticket_cost: float = (
                float(self.route.base_price_seat) + float(self.route.price_premium_seat))
            list_tickets.append(premium_ticket_cost)
        self.premium_sold_tickets: List = list_tickets

    def generate_igv_economic_tickets(self):
        """
        Adiciona a los valores de nuestra lista de tickets económicos el IGV del mismo
        """
        economic_tickets_igv = list(
            map(lambda x: round(x + IGV_TOTAL * x / 100, 2), self.economic_sold_tickets))
        return economic_tickets_igv

    def generate_igv_premium_tickets(self):
        """
        Adiciona a los valores de nuestra lista de tickets premium el IGV del mismo
        """
        premium_tickets_igv = list(
            map(lambda x: round(x + IGV_TOTAL * x / 100, 2), self.premium_sold_tickets))
        return premium_tickets_igv

    def convert_premium_tickets_igv(self):
        """
        Multiplica a los valores de nuestra lista de tickets premium el IGV
        """
        premium_tickets_igv = list(
            map(lambda x: round(IGV_TOTAL * x / 100, 2), self.premium_sold_tickets))
        return premium_tickets_igv

    def convert_economic_tickets_igv(self):
        """
        Multiplica a los valores de nuestra lista de tickets economicos el IGV
        """
        economic_tickets_igv = list(
            map(lambda x: round(IGV_TOTAL * x / 100, 2), self.economic_sold_tickets))
        return economic_tickets_igv
