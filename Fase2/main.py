from flask import request, jsonify
from flask_cors import CORS
import os.path
import lecturaEntrada
class Index:
    
    
    def __init__ (self, opcion):
        self.opcion=opcion

def main():
        var=lecturaEntrada.Carga_archivo()
       
        menu='''Menu Principal:
        1.- Cargar Archivo
        2.- Elejir ciudad
        3.- Elejir robot
        4.- Mostrar Grafica
        5.- Salir'''

        while True:
            print(menu)
            op=input("Ingrese una opcion: ")

            if op == '1':               
               var.archivoCarga()

            elif op == '2':  
                rt=input("Ingrese el nombre de la ciudad: ")
                var.cargaCiudad(rt)

                          
            elif op == '3':
                rt=input("Ingrese el nombre del robot: ")
                #var.elegirRobot(rt)
                print("Ingrese coordenada de entrada: \n")
                x=input("X: ")
                y=input("Y: ")
                var.buscar(x,y)
                
                

            elif op == '4':
               
                print("Ordenes en cola: ")#mostrar
            
            elif op == '5':
                break
            else:
                print("Opcion Invalida")
                #break

    


if __name__ == "__main__":
    main()
