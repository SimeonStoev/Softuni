from project_exer2.customer import Customer
from project_exer2.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if MovieWorld.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def get_customer_by_id(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

    def get_dvd_by_id(self, id):
        for dvd in self.dvds:
            if dvd.id == id:
                return dvd
        return None

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_customer_by_id(customer_id)
        dvd = self.get_dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd not in customer.rented_dvds and dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_customer_by_id(customer_id)
        dvd = self.get_dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += repr(customer) + "\n"
        for dvd in self.dvds:
            result += repr(dvd) + "\n"
        return result.strip()
