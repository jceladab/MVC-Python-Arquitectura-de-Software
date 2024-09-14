class InventoryView:

    @staticmethod
    def display_products(products):
        if not products:
            print("El inventario está vacío")
        else:
            print("Inventario actual: ")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product.quantity} unidades de {product.name}")

    @staticmethod
    def prompt_for_product():
        name = input("Introduce el producto: ")
        quantity = int(
            input("Introduce la cantidad de unidades del producto: "))
        return name, quantity
