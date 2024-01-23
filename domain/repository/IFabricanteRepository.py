from edomain.repository.IRepository import IRepository

from model import Fabricante

### Principio: Single Responsability
class IFabricanteRepository (IRepository):

    def insert(self, entity: Fabricante):
        pass

    def update(self, entity: Fabricante):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        pass