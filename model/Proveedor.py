from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class ProveedorData():
    nombreProveedor: str


class Proveedor(BaseModel, ProveedorData):
    pass
