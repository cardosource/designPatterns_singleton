class CheckSanidade:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not CheckSanidade.__instance:
            CheckSanidade.__instance =  super(CheckSanidade, cls).__new__(cls , *args, **kwargs)
        return CheckSanidade.__instance

    def __init__(self) :
        self.__servidores =  []
    
    def verificar_integridade(self, srv):
           print(f' Status  [Okay ] ...     {self.__servidores[srv] }')


    def  add_plataforma(self):
            self.__servidores .append('Red Hat')
            self.__servidores.append('Ubunto Server')
            self.__servidores.append('Suse')
            self.__servidores.append("Cent'Os ")
            self.__servidores.append('Fedora Server')
            


server_1 = CheckSanidade()
server_2 = CheckSanidade()



server_1.add_plataforma()
print("Controlando status de verificação de servidores A")


for  server in range(4):
    server_1.verificar_integridade(server)



server_2.add_plataforma()
print("Controlando status de verificação de servidores B")


for  server in range(4):
    server_2.verificar_integridade(server)