from unittest import TestCase

from domainimpl.ProductoRepositoryImpl import ProductoRepositoryImpl
from model.Producto import Producto


class TestProductoRepositoryImpl(TestCase):

    def test_insert(self):
        producto_to_insert = Producto(
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
        #print(producto_to_insert)
        repository = ProductoRepositoryImpl()
        producto = repository.insert(producto_to_insert)
        print("PRODUCTO", producto)

    def test_findAll(self):
        repository = ProductoRepositoryImpl()
        productos = repository.findAll()
        print(productos)
        ##assert False
