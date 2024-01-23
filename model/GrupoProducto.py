from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class GrupoProductoData():
    codGrupoProducto: str
    nombreGrupoProducto: str


class GrupoProducto(BaseModel, GrupoProductoData):
    pass
