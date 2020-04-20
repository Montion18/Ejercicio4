class FechaHora:
    __dia=''
    __mes=''
    __anio=''
    __hora=''
    __minuto=''
    __segundos=''
    

    def __init__(self,dia,mes,anio,hora,min,seg):
       self.__dia=dia
       self.__mes=mes
       self.__anio=anio
       self.__hora=hora
       self.__minuto=min
       self.__segundos=seg


    def Mostrar(self):
        print("\nDia: {} Mes: {} Año: {} Hora: {} Min: {} Seg: {} \n".format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundos))

    def PonerEnHora(self,h=0,m=0,s=0):
        self.__hora=h
        self.__minuto=m
        self.__segundos=s
    def AdelantarHora(self,h=0,m=0):
        self.__hora+=h
        self.__minuto+=m
