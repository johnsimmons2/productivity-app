from abc import abstractmethod
from psycopg2.extras import DictRow
from model import Entity, ResultDto
from database.repo.dbconnection import connect


class DBRepoProvider:
    @classmethod
    def execute_command(cls, sql: str) -> ResultDto:
        connection = connect()
        result = connection.execute_command(sql)
        if result.success and result.data:
            result.entities = cls.handle(result.data)
        return result
    
    @classmethod
    def insert(cls, data: Entity):
        params = cls._getInsertParameters(data)
        sql = '''INSERT INTO public.{0}({1})
            VALUES ({2});'''.format(params[0], params[1], params[2])
        return cls.execute_command(sql)

    @classmethod
    def get(cls, id: str):
        tableName = cls._getTableName()
        sql = "SELECT * FROM public.{0} WHERE id='{1}';".format(tableName, id)
        return cls.execute_command(sql)
    
    @classmethod
    def getMany(cls, ids: list[str]):
        tableName = cls._getTableName()
        sql = "SELECT * FROM public.{0} WHERE id in ({1});".format(tableName, ','.join(f"'{x}'" for x in ids))
        return cls.execute_command(sql)

    @classmethod
    def getAll(cls):
        tableName = cls._getTableName()
        sql = "SELECT * FROM public.{0};".format(tableName)
        return cls.execute_command(sql)

    @classmethod
    def handle(cls, qresult: DictRow | list) -> list[Entity]:
        result = []
        if type(qresult) == list:
            for row in qresult:
                result.append(cls.handle(row))
        if type(qresult) == DictRow:
            result.append(cls._mapColumnsToEntity(qresult))
        return result

    @classmethod
    def _getInsertParameters(cls, data) -> tuple:
        cols = cls._getColumnNames()
        return (cls._getTableName(),
            ','.join(f'"{str(w)}"' for w in cols),
            ','.join(f"'{str(w)}'" for w in cls._mapEntityToColumns(data, cols)))

    @classmethod
    @abstractmethod
    def _mapEntityToColumns(cls, entity: Entity, columns: list) -> list:
        pass

    @classmethod
    @abstractmethod
    def _mapColumnsToEntity(cls, row: dict) -> Entity:
        pass

    @classmethod
    @abstractmethod
    def _getEntityFromResult(cls, result: ResultDto):
        pass

    @classmethod
    @abstractmethod
    def _mapDataAndColumns(cls, data: Entity, cols: dict):
        pass

    @classmethod
    @abstractmethod
    def _getColumnNames(cls):
        pass

    @classmethod
    @abstractmethod
    def _getTableName(cls):
        pass