class Principal(type):
    def __call__(cls,  *args, **kwargs):
        print(f' - Argumentos  : {args}')
        return type.__call__(cls,   *args, **kwargs)
  #      return super().__call__(*args, **kwds):



class Segunda(metaclass=Principal):
    def __init__(self,valor, segundoValor):
        self.valor = valor
        self.segundoVal = segundoValor


artefato = Segunda(31,13)
print(artefato)


class MetaSingleton(type):
    __instance = {}
    def __call__(self, *args, **kwargs):
        if self  not in self.__instance:
            self.__instance[self] = super(MetaSingleton, self).__call__( *args, **kwargs)
        return self.__instance[self]


class Sistematizado(metaclass=MetaSingleton):
    pass

sistema_livre = Sistematizado()

print(f"Liberdade 1 {id(sistema_livre)}")

openSource  = Sistematizado()
print(f"Livre  1 {id(openSource)}")