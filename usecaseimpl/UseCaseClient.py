from domainimpl.ProductoRepositoryImpl import ProductoRepositoryImpl
from usecaseimpl.ProductoServiceImpl import ProductoServiceImpl

class UseCaseClient:

    def obtenerProductoServiceImpl(self):
        repository = ProductoRepositoryImpl()
        return ProductoServiceImpl(repository)