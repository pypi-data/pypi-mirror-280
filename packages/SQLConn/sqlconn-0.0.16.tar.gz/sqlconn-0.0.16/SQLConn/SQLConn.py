from pandas import read_sql
import warnings
from sqlalchemy import create_engine
from abc import ABC, abstractmethod
import pymysql
import pymssql
import psycopg2
import sqlite3
from typing import Union

class SQLConn(ABC):
    def __init__(self):
        warnings.filterwarnings('ignore', category=DeprecationWarning)
    def __del__(self)->None:
        if self._conn:
            self._conn.close()
    @property
    @abstractmethod
    def URL(self)->str:
        pass
    @property
    def engine(self):
        return create_engine(self.URL)
    def to_DataFrame(self,cmd:str):
        if not (cmd.lower().startswith('select') or cmd.lower().startswith('show')):
            raise ValueError("to_DataFrame does only supports 'select' or 'show' commands.")
        return read_sql(cmd,self._conn)

    def execute(self,cmd:str):
        if cmd.lower().startswith('select'):
            raise ValueError("execute does not support 'select' operations. Use 'to_DataFrame' method for queries.")
        if cmd.lower().startswith('show'):
            raise ValueError("execute does not support 'show' operations. Use 'to_DataFrame' method for queries.")
        try:
            cur=self._conn.cursor()
            cur.execute(cmd)
            self._conn.commit()
        except Exception as e:
            warnings.warn(str(e))

    def to_csv(self, cmd:str, file_name:str,encoding:str="utf-8"):
        try:
            self.to_DataFrame(cmd).to_csv(file_name+".csv", index=False,encoding=encoding)
        except Exception as e:
            warnings.warn(str(e))

    def to_excel(self, cmd:str, file_name:str):
        try:
            self.to_DataFrame(cmd).to_excel(file_name+".xlsx", index=False)
        except Exception as e:
            warnings.warn(str(e))

    def to_tsv(self, cmd:str, file_name:str,encoding:str="utf-8"):
        try:
            self.to_DataFrame(cmd).to_csv(file_name+".tsv", sep="\t",index=False,encoding=encoding)
        except Exception as e:
            warnings.warn(str(e))
    def to_sql(self,cmd:str,name:str,other):
        if not (cmd.lower().startswith('select') or cmd.lower().startswith('show')):
            raise ValueError("to_sql does only supports 'select' or 'show' commands.")
        try:
            with other.engine.connect() as conn:
                self.to_DataFrame(cmd).to_sql(name,conn,index=False,if_exists="replace")
        except Exception as e:
            warnings.warn(str(e))
    def to_HTML(self,cmd:str,escape:bool=True):
        if not (cmd.lower().startswith('select') or cmd.lower().startswith('show')):
            raise ValueError("to_HTML does only supports 'select' or 'show' commands.")
        return self.to_DataFrame(cmd).to_html(index=False,escape=escape)
    @property
    def conn(self):
        return self._conn
class MYSQLConn(SQLConn):
    def __init__(self,password:str,host:str='127.0.0.1',user:str="root",database:str="mysql",port:Union[str,int]=3306) -> None:
        super().__init__()
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__port=int(port)
        self._conn=pymysql.connect(host=self.__host,user=self.__user,password=self.__password,database=self.__database,port=self.__port)
        
    @property
    def URL(self):
        return f'mysql+pymysql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}'
class MSSQLConn(SQLConn):
    def __init__(self,password:str,host:str='127.0.0.1',user:str="sa",database:str="master",port:Union[str,int]=1433) -> None:
        super().__init__()
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__port=int(port)
        self._conn=pymssql.connect(host=self.__host,user=self.__user,password=self.__password,database=self.__database,port=self.__port)
        
    @property
    def URL(self):
        return f'mssql+pyodbc://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}'

class PostgresqlConn(SQLConn):
    def __init__(self,password:str,host:str='127.0.0.1',user:str="postgres",database:str="postgres",port:Union[str,int]=5432) -> None:
        super().__init__()
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__port=int(port)
        self._conn=psycopg2.connect(host=self.__host,user=self.__user,password=self.__password,database=self.__database,port=self.__port)
        
    @property
    def URL(self):
        return f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}'
class SQLiteConn(SQLConn):
    def __init__(self,file_path:str) -> None:
        super().__init__()
        self.__file_path=file_path
        self._conn=sqlite3.connect(file_path)
        
    @property
    def URL(self):
        return f'sqlite://{self.__file_path}'