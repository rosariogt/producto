import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.Producto import Producto
from usecaseimpl.ProductoServiceImpl import ProductoServiceImpl
from model.GrupoProducto import GrupoProducto
from usecaseimpl.GrupoProductoServiceImpl import GrupoProductoServiceImpl
from model.Proveedor import Proveedor
from usecaseimpl.ProveedorServiceImpl import ProveedorServiceImpl
from model.Fabricante import Fabricante
from usecaseimpl.FabricanteServiceImpl import FabricanteServiceImpl
from usecaseimpl.UseCaseClient import UseCaseClient

print(sys.path)

app = FastAPI()
app.title = 'My app'
app.version = '0.0.1'

origins = ["*"]
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

services = UseCaseClient()
@app.get("/", tags= ['home'])
def read_root():
    return {"Hello": "World"}


@app.post("/producto")
def crear_producto(producto: Producto):
    productoService = services.obtenerProductoServiceImpl()
    return productoService.registrarProducto(producto)

@app.post("/grupo_producto")
def crear_grupo_producto(grupoProducto: GrupoProducto):
    grupoProductoService = services.obtenerGrupoProductoServiceImpl()
    return grupoProductoService.registrarGrupoProducto(grupoProducto)

@app.post("/proveedor")
def crear_proveedor(proveedor: Proveedor):
    proveedorService = services.obtenerProveedorServiceImpl()
    return proveedorService.registrarProveedor(proveedor)
    
@app.post("/fabricante")
def crear_fabricante(fabricante: Fabricante):
    fabricanteService = services.obtenerFabricanteServiceImpl()
    return fabricanteService.registrarFabricante(fabricante)

