from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class ProductoData():
    sku: str
    nombre: str
    nombreExtranjero: str
    codGrupoProducto: str
    nombreGrupoProducto: str
    skuFabricante: str
    nmbFabricante: str
    nmbProveedor: str
    peso: int
    um: str
    precioLista: int
    codBarra: str
    skuAlternante: str


class Producto(BaseModel, ProductoData):
    pass
