from typing import List

from eusecase.impl.ResponseObject import ResponseObject
from eusecaseimpl.UsecaseImpl import UsecaseImpl

from domain.repository.IGrupoProductoRepository import IGrupoProductoRepository
from model.GrupoProducto import GrupoProducto
from usecase.IGrupoProductoService import IGrupoProductoService


class GrupoProductoServiceImpl(IGrupoProductoService, UsecaseImpl):

    ## Uso del principio de:    INVERSION DE DEPENDENCIA
    ## los modulos de alto nivel dependen de abstracciones
    def __init__(self, repository: IGrupoProductoRepository):
        self.repository = repository

    def registrarGrupoProducto(self, grupoProducto: GrupoProducto):
        grupoProducto = self.repository.insert(grupoProducto)
        response = ResponseObject(object=grupoProducto, transaction=True, messages=[])
        return response

