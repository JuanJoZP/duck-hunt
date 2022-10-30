import harperdb
import os

from typing import List
from custom_types import Score

from dotenv import load_dotenv
load_dotenv()  # loads the .env file


class Scores:
    def __init__(self, schema="duck_hunt", table="scores"):
        self.schema = schema
        self.table = table
        self.db = harperdb.HarperDB(
            url=os.environ["DB_URL"],
            username=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"])

    def insertScore(self, name: str, score: int) -> None:
        self.db.insert(self.schema, self.table, [
            {"name": name, "score": score}])
        # toca cambiarlo:
        # si la persona ya tiene un score en la tabla
        # en vez de volverla a añadir modificar su score

    def getTopScores(self) -> List[Score]:
        return self.db.sql(
            f"select id, name, score, __createdtime__ from {self.schema}.{self.table} order by score desc limit 10")
