from model import ResultDto
from config import config
import psycopg2

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
            cur = self.connection.cursor()
            cur.execute(sql)
            self.connection.commit()
            try:
                result.rowcount = cur.rowcount
                result.statusmessage = cur.statusmessage
                result.data = cur.fetchall()
            except (psycopg2.ProgrammingError) as error:
                pass
            result.success = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            result.errors.append(error)
        return result
    
    def close(self):
        self.connected = False
        try:
            self.connection.close()
        except:
            pass

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
        print(error)
    return connection

def _default_params():
    params = {}
    # TODO: Environment / Config manager should make this easier
    startupParams = config('startup')
    if startupParams['environment'] == 'dev':
        params = config('dbconfig')
    return params