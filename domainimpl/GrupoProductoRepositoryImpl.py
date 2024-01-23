from edomainimpl.postgres.Pgconnection import Pgconnection

from domain.repository.IGrupoProductoRepository import IGrupoProductoRepository
from model.GrupoProducto import GrupoProducto, GrupoProductoData


class GrupoProductoRepositoryImpl(IGrupoProductoRepository):

    def insert(self, entity: GrupoProducto):
        try:
            sql_insert = (
                f"INSERT INTO public.grupo_producto (cod_grupo_producto, nombre_grupo_producto) "
                f"VALUES('{entity.codGrupoProducto}','{entity.nombreGrupoProducto}') ")

            connection = Pgconnection()
            conn = connection.datasource_pg()
            cur = conn.cursor()
            print(entity)
            cur.execute(sql_insert)
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Excepcion al insertar el grupo producto: {e}", e.__cause__)
        return entity

    def update(self, entity: GrupoProducto):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        grupoProductos = []
        connection = Pgconnection()
        conn = connection.datasource_pg()
        cur = conn.cursor()
        cur.execute('select * FROM public.grupo_producto')
        rows = cur.fetchall()
        for row in rows:
            grupoProducto = GrupoProductoData(*row)
            grupoProductos.append(grupoProducto)
        cur.close()
        return grupoProductos
