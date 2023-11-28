from models.ClimaModel import *
from sqlmodel import select

class ClimaService():

    def __init__(self, db) -> None:
        self.db = db

    def create_clima(self, clima: ClimaCreate):
        with self.db:
            db_clima = Clima.from_orm(clima)
            self.db.add(db_clima)
            self.db.commit()
            self.db.refresh(db_clima)
            return db_clima
        
    def get_clima_by_pais_ciudad(self, pais:str, ciudad: str):
        with self.db:
            statement = select(Clima).where(Clima.pais == pais, Clima.ciudad == ciudad)
            result = self.db.exec(statement).first()
            return result
        
