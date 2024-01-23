from abc import abstractmethod
from typing import List

from eusecase.IUsecase import IUsecase

from model.Proveedor import Proveedor


class IProveedorService(IUsecase):

    @abstractmethod
    def registrarProveedor(self, proveedor: Proveedor):
        pass

