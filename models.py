from pydantic import BaseModel

class Movie(BaseModel):
    Autor: str
    Descripcion: str
    Fecha_de_Estreno: str