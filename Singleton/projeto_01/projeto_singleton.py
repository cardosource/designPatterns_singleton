import sqlite3


class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):

        if cls    not  in cls.__instances :
            cls.__instances[cls] = super(Singleton, cls).__call__( *args, **kwargs) 
        return cls.__instances[cls]



class DataMani(metaclass = Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            print("[  -  ] :  Não há conexão\n[  +  ] :  Construindo nova estrutura")
            self.connection = sqlite3.connect('fortnite_db')
            self.cursor = self.connection.cursor()
        return self.cursor

    
dbA = DataMani().connect()

dbB = DataMani().connect()
