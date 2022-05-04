import lector
class nodo:


    def __init__(self, palabra, tipo):
        self.palabra=palabra
        self.tipo=tipo
        self.siguiente=None
        self.principio=None
        self.fin=None


class colita:
    var=lector.cola()

    def __init__(self):
        self.inicio=None

    def push(self, palabra, tipo):
       	
        if self.inicio==None:
            #tm=int(self.tiempoUltimo)+int(tiempo)
            nuevo=nodo(palabra, tipo)
            self.inicio=nuevo
            self.inicio.principio=nuevo
            nuevo.fin=nuevo
            

        else:
            nuevo=nodo(palabra, tipo)
            aux=self.posicion()
            aux.siguiente=nuevo
            nuevo.fin=nuevo

    def posicion(self):
        ultimo=self.inicio

        while ultimo.siguiente != None:
            ultimo=ultimo.siguiente

        return ultimo

    def recorrer(self,pl):
        aux=self.inicio
        while aux != None:

            print("Palabra: "+aux.palabra+" - Tipo "+str(aux.tipo))
            aux=aux.siguiente

    def descomponer(self, frase):
        cadena = frase.split()
        fecha = "algo"
        mensajes=0
        pos=0
        neg=0
        empresa=0


        for x in cadena:
            aux=self.inicio
            while aux != None:
                if(x == aux.palabra):
                    if (aux.tipo == "positivo"):
                        pos=pos+1
                    elif (aux.tipo == "negativo"):
                        neg=neg+1
                    elif (aux.tipo == "empresa"):
                        empresa=aux.palabra

                aux=aux.siguiente

        if (pos>neg):
            self.var.subir(fecha,empresa,0,1,0,0)
            #pos = 1 neg =0
        elif(pos<neg):
            self.var.subir(fecha,empresa,0,0,1,0)
            #pos = 0 neg =1
        else:
            self.var.subir(fecha,empresa,0,0,0,1)
            #neutro =1

        #print(cadena)
        self.var.mostrar()
        

    def mostrar(self):
        aux=self.inicio
        while aux != None:despliege y distribucion
            print("empresa: "+ str(aux.empresa))
            aux=aux.siguiente
