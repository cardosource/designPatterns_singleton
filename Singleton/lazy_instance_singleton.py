

class  Singleton:
    __instance = None

    def __init__(self) :
        if not Singleton.__instance:
            print('O método __init___ foi invocado')
        else:
            print(f'A instanacia ja foi feita {self.get_Instance()}')

    @classmethod
    def get_Instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton()


print(f'Objeto criado {Singleton.get_Instance()}')
s2 = Singleton()