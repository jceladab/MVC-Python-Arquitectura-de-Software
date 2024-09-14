from controller import InventoryController
from view import InventoryView


def main():
    controller = InventoryController()
    view = InventoryView()

    while True:
        print("\nSistema de inventario")
        print("1. Agregar Producto")
        print("2. Listar inventario")
        print("3. Salir del programa")
        action = input("Seleccione una opción: ")

        if action == '1':
            name, quantity = view.prompt_for_product()
            controller.add_product(name, quantity)
        elif action == '2':
            products = controller.get_products()
            view.display_products(products)
        elif action == '3':
            print("Saliendo...")
            break


if __name__ == '__main__':
    main()
