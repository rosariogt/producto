from eusecase.impl.ResponseObject import ResponseObject
from eusecaseimpl.UsecaseImpl import UsecaseImpl

from domainimpl.ProductoRepositoryImpl import ProductoRepositoryImpl
from model.Producto import Producto
from usecase.IProductoService import IProductoService


class ProductoServiceImpl(IProductoService, UsecaseImpl):

    def registrarProducto(self, producto: Producto):
        productoRepository = ProductoRepositoryImpl()
        producto = productoRepository.insert(producto)
        print("-------------------")
        response = ResponseObject(object=producto, transaction=True, messages=[])
        return response

