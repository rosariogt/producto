from edomain.repository.IRepository import IRepository

from model import Producto


class IProductoRepository (IRepository):

    def insert(self, entity: Producto):
        pass

    def update(self, entity: Producto):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        pass