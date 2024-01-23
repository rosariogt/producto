from abc import abstractmethod
from typing import List

from eusecase.IUsecase import IUsecase

from model.Fabricante import Fabricante


class IFabricanteService(IUsecase):

    @abstractmethod
    def registrarFabricante(self, fabricante: Fabricante):
        pass

