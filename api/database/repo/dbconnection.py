from typing import OrderedDict
from model import ResultDto
from config import config
from extra.logging import Logger
import psycopg2
from psycopg2.extras import DictCursor, DictRow

DEFAULT_TIMEOUT = 30

class Connection:
    def __init__(self, db: str, user: str, conn: any = None):
        self.db = db
        self.user = user
        self.connected = False
        self.succeeded = False
        self.connection = conn

    def execute_command(self, sql: str):
        result = ResultDto()
        if not self.connected:
            result.statusmessage = 'CONNECTION ERROR'
            result.errors.append('Connection request failed. Cannot execute command.')
            return result
        try:
            self.connection.cursor_factory = DictCursor
            cur = self.connection.cursor()
            cur.execute(sql)
            self.connection.commit()
            try:
                result.rowcount = cur.rowcount
                result.statusmessage = cur.statusmessage
                raw = cur.fetchall()
                result.data = self._compress(raw)
            except (psycopg2.ProgrammingError) as error:
                pass
            result.success = True
        except (Exception, psycopg2.DatabaseError) as error:
            Logger.error(error)
            result.errors.append(error)
        return result
    
    def close(self):
        self.connected = False
        try:
            self.connection.close()
        except:
            pass

    def _compress(self, data: any):
        if isinstance(data, DictRow):
            return data
        if isinstance(data, list):
            if len(data) == 0:
                return None
            elif len(data) == 1:
                return self._compress(data[0])
            else:
                return list(map(self._compress, data))
        elif isinstance(data, tuple):
            if len(data) == 1:
                return data[0]
        return data

def connect(**params) -> Connection:
    if params is None or len(params) == 0:
        params = _default_params()
    params['connect_timeout'] = DEFAULT_TIMEOUT
    connection = Connection(params['database'], params['user'])
    try:
        conn = psycopg2.connect(**params)
        connection.connection = conn
        connection.connected = True
        connection.succeeded = True
    except Exception as error:
        Logger.error(error)
    return connection

def _default_params():
    params = config('dbconfig')
    return params