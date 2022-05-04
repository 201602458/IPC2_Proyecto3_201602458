class nodo:

    def __init__(self, fecha, empresa ,mensajes, positivos, negativos, neutros):
        self.fecha=fecha
        self.empresa=empresa
        self.mensajes=mensajes
        self.positivos=positivos
        self.negativos=negativos
        self.neutros=neutros
        self.siguiente=None
        self.principio=None
        self.fin=None

class cola:
    def __init__(self):
        self.inicio=None

    def subir(self, fecha, empresa ,mensajes, positivos, negativos, neutros):
       	
        if self.inicio==None:
            #tm=int(self.tiempoUltimo)+int(tiempo)
            nuevo=nodo(fecha, empresa ,mensajes, positivos, negativos, neutros)
            self.inicio=nuevo
            self.inicio.principio=nuevo
            nuevo.fin=nuevo
            

        else:
            nuevo=nodo(fecha, empresa ,mensajes, positivos, negativos, neutros)
            aux=self.posicion()
            aux.siguiente=nuevo
            nuevo.fin=nuevo

    def posicion(self):
        ultimo=self.inicio

        while ultimo.siguiente != None:
            ultimo=ultimo.siguiente

        return ultimo

    def mostrar(self):
        aux=self.inicio
        while aux != None:
            print("empresa: "+ str(aux.empresa))
            print("total mensajes: "+ str(self.totalM(aux.empresa)))
            print("total positivos: "+ str(aux.positivos))
            print("total negativos: "+ str(aux.negativos))
            print("total neutros: "+ str(aux.neutros))
            aux=aux.siguiente

    def totalM(self, empresa):
        total=0

        aux=self.inicio
        while aux != None:
            if(empresa==aux.empresa):
                total=total+1

            aux=aux.siguiente
        return total

