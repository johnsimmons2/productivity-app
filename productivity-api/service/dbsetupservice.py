from config import config
from database import connect
from definitions import ROOT_PATH
import glob
import os

class ServiceChain:
    def __init__(self):
        self.succeed = False

    def first(self, cmd: any):
        result = cmd()
        if result is not None and isinstance(result, bool):
            self.succeed = result
        else:
            self.succeed = True
        return self

    def then(self, cmd: any):
        return self.first(cmd)

            

class DBSetupService:
    TABLES = ['users', 'transactions']
    DATABASE_NAME = 'productivity'

    @classmethod
    def start(cls):
        ServiceChain().first(cls._verifypadmin) \
            .then(cls._verifydb)                \
            .then(cls._verifytables)

    @staticmethod
    def _verifydb():
        connection = connect(database='postgres', user='postgres', password='root')
        connection.connection.autocommit = True

        verifyDb = connection.execute_command("SELECT EXISTS (SELECT FROM pg_database WHERE datname = 'productivity');")
        if verifyDb.data == False:
            createDb = connection.execute_command(DBSetupService._get_migration('setup', 'db'))
            if createDb.success == False:
                print('Failed to run DB Setup Migration.')
            connection.close()
            return createDb.success
        return True

    @staticmethod
    def _verifypadmin():
        connection = connect(database='postgres', user='postgres', password='root')
        connection.connection.autocommit = True
        createpadmin = connection.execute_command(DBSetupService._get_migration('setup', 'padmin'))
        
        if createpadmin.success == False:
            print('Failed to run DB Setup Migration.')
        connection.close()
        return createpadmin.success

    @staticmethod
    def _verifytables():
        connection = connect()
        for table in DBSetupService.TABLES:
            tableExists = connection.execute_command("select exists(select * from information_schema.tables where table_name='{0}')".format(table))
            if tableExists.data == False:
                createTable = connection.execute_command(DBSetupService._get_migration('table', table))
        connection.close()
    
    @staticmethod
    def _get_migration(entityType: str, name: str, migrationType: str = 'create'):
        path = 'database\\sql\\{0}\\*{1}.sql'.format(entityType, name)
        globs = glob.glob(path, root_dir=ROOT_PATH)
        if len(globs) > 0:
            for path in globs:
                if migrationType in path:
                    file = open(ROOT_PATH + "\\" + path)
                    sql = file.read()
                    return sql


