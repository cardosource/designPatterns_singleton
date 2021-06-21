class SingletonClass(object):
  def __new__(cls):
          if not hasattr(cls, 'instance'):
                    cls.instance = super(SingletonClass, cls).__new__(cls)
                    print(f'Criando Objeto {cls.instance}')

          return cls.instance

    
singleton1 = SingletonClass()  
singleton2 = SingletonClass()

print(f"Instancia 1 {id(singleton1)}")
print(f"Instancia 2 {id(singleton2)}")