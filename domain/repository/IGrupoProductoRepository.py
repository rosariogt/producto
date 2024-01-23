from edomain.repository.IRepository import IRepository

from model import GrupoProducto

### Principio: Single Responsability
class IGrupoProductoRepository (IRepository):

    def insert(self, entity: GrupoProducto):
        pass

    def update(self, entity: GrupoProducto):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        pass