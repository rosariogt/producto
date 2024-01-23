from typing import List

from eusecase.impl.ResponseObject import ResponseObject
from eusecaseimpl.UsecaseImpl import UsecaseImpl

from domain.repository.IFabricanteRepository import IFabricanteRepository
from model.Fabricante import Fabricante
from usecase.IFabricanteService import IFabricanteService


class FabricanteServiceImpl(IFabricanteService, UsecaseImpl):

    ## Uso del principio de:    INVERSION DE DEPENDENCIA
    ## los modulos de alto nivel dependen de abstracciones
    def __init__(self, repository: IFabricanteRepository):
        self.repository = repository

    def registrarFabricante(self, fabricante: Fabricante):
        fabricante = self.repository.insert(fabricante)
        response = ResponseObject(object=fabricante, transaction=True, messages=[])
        return response
