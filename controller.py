from model import InventoryModel, Product


class InventoryController:
    def __init__(self):
        self.model = InventoryModel()

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.model.add_product(product)

    def get_products(self):
        return self.model.get_products()
