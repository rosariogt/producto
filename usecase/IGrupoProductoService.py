from abc import abstractmethod
from typing import List

from eusecase.IUsecase import IUsecase

from model.GrupoProducto import GrupoProducto


class IGrupoProductoService(IUsecase):

    @abstractmethod
    def registrarGrupoProducto(self, grupoProducto: GrupoProducto):
        pass
