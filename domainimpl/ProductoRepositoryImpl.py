from edomainimpl.postgres.Pgconnection import Pgconnection

from domain.repository.IProductoRepository import IProductoRepository
from model.Producto import Producto, ProductoData


class ProductoRepositoryImpl(IProductoRepository):

    def insert(self, entity: Producto):
        try:
            sql_insert = (
                f"INSERT INTO public.producto (sku, nombre, nombre_extranjero, cod_grupo_producto, nombre_grupo_producto, sku_fabricante, nmb_fabricante, nmb_proveedor, peso, um, precio_lista, cod_barra, sku_alternante) "
                f"VALUES('{entity.sku}','{entity.nombre}','{entity.nombreExtranjero}','{entity.codGrupoProducto}','{entity.nombreGrupoProducto}','{entity.skuFabricante}','{entity.nmbFabricante}','{entity.nmbProveedor}',{entity.peso},'{entity.um}',{entity.precioLista},'{entity.codBarra}','{entity.skuAlternante}') ")

            connection = Pgconnection()
            conn = connection.datasource_pg()
            cur = conn.cursor()
            print(entity)
            cur.execute(sql_insert)
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Excepcion al insertar el producto: {e}", e.__cause__)
        return entity

    def update(self, entity: Producto):
        pass

    def findById(self, id: int):
        pass

    def findAll(self):
        productos = []
        connection = Pgconnection()
        conn = connection.datasource_pg()
        cur = conn.cursor()
        cur.execute('select * FROM public.producto')
        rows = cur.fetchall()
        for row in rows:
            producto = ProductoData(*row)
            productos.append(producto)
        cur.close()
        return productos
