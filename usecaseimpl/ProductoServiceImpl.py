from eusecase.impl.ResponseObject import ResponseObject
from eusecaseimpl.UsecaseImpl import UsecaseImpl

from domain.repository.IProductoRepository import IProductoRepository
from model.Producto import Producto
from usecase.IProductoService import IProductoService


class ProductoServiceImpl(IProductoService, UsecaseImpl):

    ## Uso del principio de:    INVERSION DE DEPENDENCIA
    ## los modulos de alto nivel dependen de abstracciones
    def __init__(self, repository: IProductoRepository):
        self.repository = repository

    def registrarProducto(self, producto: Producto):
        producto = self.repository.insert(producto)
        print("-------------------")
        response = ResponseObject(object=producto, transaction=True, messages=[])
        return response

