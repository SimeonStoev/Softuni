from itertools import groupby

from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        lines = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            f"{self.get_estimated_profit()}",
            "**Furniture for sale:",
        ]

        sorted_products = sorted(self.products, key=lambda p: p.model)

        for model, group in groupby(sorted_products, key=lambda p: p.model):
            prices = [p.price for p in group]
            avg_price = sum(prices) / len(prices)
            lines.append(f"{model}: {len(prices)}pcs, average price: {avg_price:.2f}")

        return "\n".join(lines).strip()
