from itertools import groupby

from project.stores.base_store import BaseStore
from project.products.base_product import BaseProduct

from project.stores.toy_store import ToyStore
from project.stores.furniture_store import FurnitureStore

from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse


class FactoryManager:
    _VALID_PRODUCT_TYPES = ["Chair", "HobbyHorse"]
    _VALID_STORE_TYPES = ['FurnitureStore', 'ToyStore']

    def __init__(self, name: str):
        self.name = name
        self.income = 0
        self.products = []
        self.stores = []

    def get_store(self, store_name: str):
        for store in self.stores:
            if store.name == store_name:
                return store
        return None

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self._VALID_PRODUCT_TYPES:
            raise Exception("Invalid product type!")

        # Code to produce the item would go here
        if product_type == "Chair":
            new_product = Chair(model, price)
        else:
            new_product = HobbyHorse(model, price)

        self.products.append(new_product)
        return f"A product of sub-type {new_product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self._VALID_STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")

        # Code to register the store would go here
        if store_type == "FurnitureStore":
            new_store = FurnitureStore(name, location)
        else:
            new_store = ToyStore(name, location)

        self.stores.append(new_store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        product_type_needed = {"FurnitureStore": "Furniture", "ToyStore": "Toys"}
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        product_type = product_type_needed[store.__class__.__name__]
        filtered_products = [product for product in products if product.sub_type == product_type]

        if len(filtered_products) == 0:
            return "Products do not match in type. Nothing sold."

        # sell products to store
        store.products.extend(filtered_products)
        # Decrease store capacity by the number of products sold
        store.capacity -= len(filtered_products)
        # Increase factory income by the total price of the sold products
        self.income += sum(product.price for product in filtered_products)
        # remove sold products from factory products list
        for product in filtered_products:
            self.products.remove(product)

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store = self.get_store(store_name)
        if not store:
            raise Exception("No such store!")

        if len(store.products):
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        product_for_model_count = sum(1 for product in self.products if product.model == product_model)
        for product in self.products:
            if product.model == product_model:
                product.discount()

        return f"Discount applied to {product_for_model_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = self.get_store(store_name)
        if not store:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        # sort products and store asc by model and store name
        self.products.sort(key=lambda product: product.model)
        self.stores.sort(key=lambda store: store.name)

        lines = [f"Factory: {self.name}", f"Income: {self.income:.2f}", "***Products Statistics***",
                 f"Unsold Products: {len(self.products)}. Total net price: {sum(product.price for product in self.products):.2f}"]

        for model, group in groupby(self.products, key=lambda product: product.model):
            number_of_products = sum(1 for product in group)
            lines.append(f"{model}: {number_of_products}")

        lines.append(f"***Partner Stores: {len(self.stores)}***")
        for store in self.stores:
            lines.append(store.name)

        return "\n".join(lines).strip()
