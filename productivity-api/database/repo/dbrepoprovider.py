from abc import abstractmethod
from collections import OrderedDict
from config import config
from model import Entity, ResultDto
from database.repo.dbconnection import connect


class DBRepoProvider:
    def execute_command(self, sql: str) -> ResultDto:
        connection = connect()
        result = connection.execute_command(sql)
        if result.success and result.data:
            result.entities = self.handle(result.data)
        return result
    
    def insert(self, data: Entity):
        params = self._getInsertParameters(data)
        sql = '''INSERT INTO public.{0}({1})
            VALUES ({2});'''.format(params[0], params[1], params[2])
        return self.execute_command(sql)

    def get(self, id: str):
        tableName = self._getTableName()
        sql = "SELECT * FROM public.{0} WHERE id='{1}';".format(tableName, id)
        return self.execute_command(sql)
    
    def getMany(self, ids: list[str]):
        tableName = self._getTableName()
        sql = "SELECT * FROM public.{0} WHERE id in ({1});".format(tableName, ','.join(f"'{x}'" for x in ids))
        return self.execute_command(sql)

    def getAll(self):
        tableName = self._getTableName()
        sql = "SELECT * FROM public.{0};".format(tableName)
        return self.execute_command(sql)

    def handle(self, qresult: OrderedDict) -> list[Entity]:
        result = []
        for row in qresult:
            entity = self._mapColumnsToEntity(row)
            result.append(entity)
        return result

    def _getInsertParameters(self, data) -> tuple:
        cols = self._getColumnNames()
        return (self._getTableName(),
            ','.join(f'"{str(w)}"' for w in cols),
            ','.join(f"'{str(w)}'" for w in self._mapEntityToColumns(data, cols)))

    @abstractmethod
    def _mapEntityToColumns(self, entity: Entity, columns: list) -> list:
        pass

    @abstractmethod
    def _mapColumnsToEntity(self, row: dict) -> Entity:
        pass

    @abstractmethod
    def _getEntityFromResult(self, result: ResultDto):
        pass

    @abstractmethod
    def _mapDataAndColumns(self, data: Entity, cols: dict):
        pass

    @abstractmethod
    def _getColumnNames(self):
        pass

    @abstractmethod
    def _getTableName(self):
        pass