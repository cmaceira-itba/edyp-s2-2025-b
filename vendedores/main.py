from vendedor import Vendedor
from venta import Venta
from empresa import Empresa

def main():
    empresa = Empresa()

    carlos = Vendedor("Carlos")
    ventas_norte_carlos = Venta("norte", 3528)
    ventas_sur_carlos = Venta("sur", 2400)
    ventas_oeste_carlos = Venta("oeste", 8200)

    carlos.agregar_venta(ventas_norte_carlos)
    carlos.agregar_venta(ventas_sur_carlos)
    carlos.agregar_venta(ventas_oeste_carlos)
    print(carlos.ventas)

    empresa.agregar_vendedor(carlos)

    print(carlos.consultar_venta("norte"))
    print(carlos.consultar_venta("este"))

    print(empresa.calcular_ventas_totales())

if __name__== "__main__":
    main()
