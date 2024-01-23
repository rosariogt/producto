import sys

from fastapi import FastAPI

from model.Producto import Producto
from usecaseimpl.ProductoServiceImpl import ProductoServiceImpl

print(sys.path)

app = FastAPI()
app.title = 'My app'
app.version = '0.0.1'

service = ProductoServiceImpl()
@app.get("/", tags= ['home'])
def read_root():
    return {"Hello": "World"}


@app.post("/producto")
def crear_producto(producto: Producto):
    return service.registrarProducto(producto)