from edomainimpl.postgres.Pgconnection import Pgconnection

from domain.repository.IProveedorRepository import IProveedorRepository
from model.Proveedor import Proveedor, ProveedorData


class ProveedorRepositoryImpl(IProveedorRepository):

    def insert(self, entity: Proveedor):
        try:
            sql_insert = (
                f"INSERT INTO public.proveedor (nmb_proveedor) "
                f"VALUES('{entity.nmbProveedor}') ")

            connection = Pgconnection()
            conn = connection.datasource_pg()
            cur = conn.cursor()
            print(entity)
            cur.execute(sql_insert)
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Excepcion al insertar el proveedor: {e}", e.__cause__)
        return entity

    def update(self, entity: Proveedor):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        proveedors = []
        connection = Pgconnection()
        conn = connection.datasource_pg()
        cur = conn.cursor()
        cur.execute('select * FROM public.proveedor')
        rows = cur.fetchall()
        for row in rows:
            proveedor = ProveedorData(*row)
            proveedors.append(proveedor)
        cur.close()
        return proveedors
