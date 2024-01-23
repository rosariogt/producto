from typing import List

from eusecase.IUsecase import IUsecase

from model.Producto import Producto


class IProductoService(IUsecase):

    def registrarProducto(self, producto: Producto):
        pass

    def registrarGrupoProducto(self, productos: List[Producto]):
        pass