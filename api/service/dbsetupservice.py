from config import config
from database import connect
from definitions import ROOT_PATH
from extra.logging import Logger
import glob
import os

class ServiceChain:
    def __init__(self):
        self.succeeded = False

    def first(self, cmd: any):
        result = cmd()
        if result is not None and isinstance(result, bool):
            self.succeeded = result
        else:
            self.succeeded = True
        return self

    def then(self, cmd: any):
        if self.succeeded:
            return self.first(cmd)
        else:
            Logger.warn('Startup migrations haulted on migration command {0}'.format(cmd))

class DBSetupService:
    TABLES = ['users', 
            'transactions', 
            'transaction_details', 
            'budgets', 
            'budget_details', 
            'schedules', 
            'categories']
    DATABASE_NAME = 'productivity'

    @classmethod
    def start(cls):
        Logger.debug('Starting migrations')
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
                Logger.error('Database did not exist but it could not be created from migrations.')
            else:
                Logger.debug('Database was successfully created.')
            connection.close()
            return createDb.success
        return True

    @staticmethod
    def _verifypadmin():
        Logger.debug('Verifying padmin')
        connection = connect(database='postgres', user='postgres', password='root')
        connection.connection.autocommit = True
        createpadmin = connection.execute_command(DBSetupService._get_migration('setup', 'padmin'))
        
        if createpadmin.success == False:
            Logger.error('Could not create padmin user role from migrations.')
        else:
            Logger.debug('padmin was verified successfully.')
        connection.close()
        return createpadmin.success

    @staticmethod
    def _verifytables():
        success = True
        connection = connect()
        for table in DBSetupService.TABLES:
            tableExists = connection.execute_command("select exists(select * from information_schema.tables where table_name='{0}')".format(table))
            if tableExists.data == False:
                createTable = connection.execute_command(DBSetupService._get_migration('table', table))
                if createTable.success == False:
                    Logger.error('Could not create table {0}.'.format(table))
                    success = False
                else:
                    Logger.debug('Created table {0}'.format(table))
            else:
                Logger.debug('Verified table {0}'.format(table))
        connection.close()
        return success
    
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


