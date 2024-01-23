from edomainimpl.postgres.Pgconnection import Pgconnection

from domain.repository.IFabricanteRepository import IFabricanteRepository
from model.Fabricante import Fabricante, FabricanteData


class FabricanteRepositoryImpl(IFabricanteRepository):

    def insert(self, entity: Fabricante):
        try:
            sql_insert = (
                f"INSERT INTO public.fabricante (sku_fabricante, nmb_fabricante) "
                f"VALUES('{entity.skuFabricante}','{entity.nmbFabricante}') ")

            connection = Pgconnection()
            conn = connection.datasource_pg()
            cur = conn.cursor()
            print(entity)
            cur.execute(sql_insert)
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Excepcion al insertar el fabricante: {e}", e.__cause__)
        return entity

    def update(self, entity: Fabricante):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        fabricantes = []
        connection = Pgconnection()
        conn = connection.datasource_pg()
        cur = conn.cursor()
        cur.execute('select * FROM public.fabricante')
        rows = cur.fetchall()
        for row in rows:
            fabricante = FabricanteData(*row)
            fabricantes.append(fabricante)
        cur.close()
        return fabricantes
