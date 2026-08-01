from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    MATERIAL = "Wood"
    SUB_TYPE = "Furniture"
    DISCOUNT_PERCENTAGE = 0.1

    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.MATERIAL, self.SUB_TYPE)

    # updates chair price with 10% discount
    def discount(self):
        self.price -= self.price * self.DISCOUNT_PERCENTAGE
