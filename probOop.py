class Producto:
    def __init__(self, nombre, precio,stock):
        self._nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        return self.precio

# Si el Stock actual es mayor a 50 unidades, aplicar un 5% de descuento addicional (acumulable).
    def descuento_stock(self, porcentaje=5):  
        if self.stock > 50:
            descuento = self.precio * (porcentaje / 100)
            self.precio -= descuento
        return self.precio
    
# Si el precio final es menor a 5.000, el sistema debe imprimir una advertencia de "Revisión de Margen Necesaria"
def advertencia_margen(producto):
    if producto.precio < 5000:
        return "Revisión de Margen Necesaria"
    else:
        return "Margen Aceptable"
class ProductoFisico(Producto):
    def __init__(self,nombre,precio,stock):
        super().__init__(nombre,precio,stock)


class ProductoDigital(Producto):
    def __init__(self,nombre,precio,stock):
        super().__init__(nombre,precio,stock)

# Si el producto es Digital, aplicar un 15% de descuento.
    def descuento_digital(self,porcentaje=15):
        return super().aplicar_descuento(porcentaje)
    


# Ejemplo de uso
producto1 = ProductoFisico("Laptop", 6000, 60)
producto1.descuento_stock()
print(f"Precio final del producto físico: {producto1.precio}")
print(advertencia_margen(producto1))
producto2 = ProductoDigital("E-book", 4000, 30)
producto2.descuento_digital()
print(f"Precio final del producto digital: {producto2.precio}")
print(advertencia_margen(producto2))
