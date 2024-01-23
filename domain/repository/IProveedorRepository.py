from edomain.repository.IRepository import IRepository

from model import Proveedor

### Principio: Single Responsability
class IProveedorRepository (IRepository):

    def insert(self, entity: Proveedor):
        pass

    def update(self, entity: Proveedor):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        pass