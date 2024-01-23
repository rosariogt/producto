from unittest import TestCase

from model.Producto import Producto
from usecaseimpl.ProductoServiceImpl import ProductoServiceImpl


class TestProductoServiceImpl(TestCase):

    def test_registrar_producto(self):
        producto = Producto(
            sku="abc",  # str
            nombre='Camisa',  # str
            nombreExtranjero='Shirt',  # str
            codGrupoProducto='abc',  # str
            nombreGrupoProducto='abc',
            skuFabricante='abv',  # str
            nmbFabricante='avf',  # str
            nmbProveedor='aff',  # str
            peso=15,  # int
            um='ag',  # str
            precioLista=1,  # int
            codBarra='agg',  # str
            skuAlternante='agg',  # str
        )
        service = ProductoServiceImpl()
        response = service.registrarProducto(producto)
        print(response)
