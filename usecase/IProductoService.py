from abc import abstractmethod
from typing import List

from eusecase.IUsecase import IUsecase

from model.Producto import Producto


class IProductoService(IUsecase):

    @abstractmethod
    def registrarProducto(self, producto: Producto):
        pass

    @abstractmethod
    def registrarGrupoProducto(self, productos: List[Producto]):
        pass