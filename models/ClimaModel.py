from typing import List, Optional

from sqlmodel import Field, SQLModel


class ClimaBase(SQLModel):
    pais: str
    ciudad: str
    velocidadViento: int
    descripcion:str
    temperaturaMaxima: int
    temperaturaMinima: int
    

class Clima(ClimaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ClimaCreate(ClimaBase):
    pass 

class ClimaRead(ClimaBase):
    id: int