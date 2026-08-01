class FactoryManager:
    _VALID_PRODUCT_TYPES = ["Chair", "HobbyHorse"]
    _VALID_STORE_TYPES = ['FurnitureStore', 'ToyStore']

    def __init__(self, name: str):
        self.name = name
        self.income = 0
        self.products = []
        self.stores = []

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
