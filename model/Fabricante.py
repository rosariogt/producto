from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class FabricanteData():
    skuFabricante: str
    nmbFabricante: str
    

class Fabricante(BaseModel, FabricanteData):
    pass
