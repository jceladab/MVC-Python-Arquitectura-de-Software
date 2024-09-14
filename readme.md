MVC - Ejemplo de patrón arquitectónico Modelo Vista Controlador.

Descrición:
    El programa es un pequeño gestor de inventario en memoria, donde tendremos dos métodos principales: add_product y get_product con los que al interactuar
    en la vista principal nos permitirá ingresar un nuevo producto y luego listarlo.

Modelo:
    El product contiene datos del nombre y la cantidad de productos y la clase InventoryModel administra la lista de productos, permitiendo añadir y listar cada uno de los elementos.

Vista: 
    Esta es responsable de mostrar la lista de los productos y solicitarle al usuario que introduzca nuevos elementos.

Controlador:
    Conecta al modelo y la vista gestionandolas y redirigiendo las acciones del usuario al módulo correspondiente.

Ejecución del método main.py:
    Sólo deberá descargar todos los archivos alojándolos en un fichero único y ejecutar a través de la consola de su preferencia.
