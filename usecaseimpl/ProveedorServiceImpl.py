from typing import List

from eusecase.impl.ResponseObject import ResponseObject
from eusecaseimpl.UsecaseImpl import UsecaseImpl

from domain.repository.IProveedorRepository import IProveedorRepository
from model.Proveedor import Proveedor
from usecase.IProveedorService import IProveedorService


class ProveedorServiceImpl(IProveedorService, UsecaseImpl):

    ## Uso del principio de:    INVERSION DE DEPENDENCIA
    ## los modulos de alto nivel dependen de abstracciones
    def __init__(self, repository: IProveedorRepository):
        self.repository = repository

    def registrarProveedor(self, proveedor: Proveedor):
        proveedor = self.repository.insert(proveedor)
        response = ResponseObject(object=proveedor, transaction=True, messages=[])
        return response
