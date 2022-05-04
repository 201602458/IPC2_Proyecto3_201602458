import xml.etree.ElementTree as ET
from xml.dom import minidom
import diccionario

class Carga_archivo:
    var=diccionario.colita()

    def __init__ (self):
            self.link="entrada.xml"
            self.archivoCarga()

    def archivoCarga(self):
        self.txt = minidom.parse(self.link)#aqui se pone el self.link
        tree = ET.parse(self.link)
        self.root = tree.getroot()

        self.diccionario()
        #self.elementos()

    def elementos(self):
        
        for elem in self.root.iter():
            #print(elem.text)#lo que hay dentro de los tags
            print(elem.tag)#los nombre de los tags
            #print(elem.attrib)#atributos dentro de tags

    
    def diccionario(self):

        #print(str(self.root[0][0].tag))#(etq)(numero)
        sent="x"

        for elem in self.root.iter():
            palabra=elem.text
            etq=elem.tag
            

            if (etq=="sentimientos_positivos"):
                sent=self.root[0][0].tag
            elif (etq=="sentimientos_negativos"):
                sent=self.root[0][1].tag
            elif (etq=="empresas_analizar"):
                sent=self.root[0][2].tag
            elif (etq=="lista_mensajes"):
                #print("entro")
                sent=self.root[1][0].tag
            
            if(sent=="sentimientos_positivos"):
                self.var.push(palabra,"positivo")
                #print(palabra)
            elif (sent=="sentimientos_negativos"):
                self.var.push(palabra,"negativo")
                #print(palabra)
            elif (sent=="empresas_analizar"):
                if (str(elem.tag)=="nombre"):
                #print(palabra)
                    self.var.push(palabra,"empresa")
                else:
                    self.var.push(palabra,"palabra")
            else:
                #print(palabra)
                self.var.descomponer(palabra)

            

        #self.var.mostrar()



            

            




