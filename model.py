class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class InventoryModel:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products
