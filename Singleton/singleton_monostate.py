class MonoState:

    __estado = {}

    def __new__(cls,  *args,  **kwargs) :
        objt = super(MonoState,  cls).__new__(cls,   *args,   **kwargs)
        objt.__dict__ = cls.__estado
        return objt


m_estado1 = MonoState()
print(f'  M1 : {id(m_estado1)}  ') 
print(m_estado1.__dict__)

m_estado2 = MonoState()

print(f'  M2 : {id(m_estado2)}  ') 
print(m_estado2.__dict__)

m_estado1.sistema = 'Open Source'
print(f' M1 : {m_estado1.__dict__}')
print(f' M2 : {m_estado2.__dict__}')