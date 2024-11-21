from datetime import datetime
import statistics

#Se define objeto Experimento
class Experimento:
    def __init__(self, nombre, fechaRealizacion, tipoExperimento, resultados):
        self.nombre=nombre
        self.fechaRealizacion=fechaRealizacion
        self.tipoExperimento=tipoExperimento
        self.resultados=resultados

#funcion para crear experimento
def gestionarExperimento(listaExperimentos):
    resultados={}
    variables=[]
    tipos=['Quimica', 'Fisica', 'Biologuia']

    #valida que nombre no en blanco
    
    nombre = input("Ingrese el nombre del experimento: ")
    if not nombre:
        print("**Debe ingresar un nombre**")
        return

    #valida fecha con formato corecto
    fechaRealizacion_str = input("Ingrese la fecha realizacion del experimento (DD/MM/YYYY): ")
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")         
    except ValueError:
        print("**fecha no valida.**")
        return
    
    # Pendiente validar que el tipo de experimento este en la lista
    print(f"De que tipo es su experimento: " )
    try:
        cont=0
        for tipo in tipos:
            cont += 1
            print(f"{cont}. {tipo}")
        tipo = int(input("Seleccione el tipo de experimento: "))
        tipoExperimento=tipos[tipo-1]        
    except IndexError:
        print("**El tipo de experimento seleccionada no existe**")
        return
    
    #pendiente validar tamaño numerico
    tamaño=int(input("Cuantas variables tiene el experimento: "))
    try:
        for i in range(0, tamaño):
            variable =input(f"ingrese la variable {i+1}: ")
            variables.append(variable)

        for variable in variables:
            print(f"Ingresa un valor para la variable {variable}, para finalizar presione cualquier letra")
            valores=[]
            
            # bucle para añadir valores por variable
            while True:
                valor = input(f"Ingresa un valor para la variable {variable}: ")
                if valor.isalpha():  # Verifica si es una letra
                    print("**El experimento solo acepta variables cuantitativas.**")
                    break
                elif not valor:
                    print("**Debe ingresar un valor**")
                else:
                    valores.append(valor)
                resultados[variable]=valores
    except tamaño.isalnum():
        print("**El valor ingresado no es numerico**")


    print(f"Se creo el experimento {nombre}, con los valores:")
    print(resultados)
    #crear un objeto y lo agrega a lista de experimentos
    experimento = Experimento(nombre, fechaRealizacion,  tipoExperimento, resultados)
    listaExperimentos.append(experimento)

#funcion para consultar experimento
def VisualizarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("no hay experimentos registradas")
        return
    
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha Realizacion: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Tipo Experimento: {experimento.tipoExperimento}")
        print(f"Resultados: {experimento.resultados}")

def menu():
    
    listaExperimentos = []
    while True:
        print("BIENVENIDO AL SISTEMA DE INVESTIGACION")
        print("1. Gestion Experimento")
        print("2. Visualizas Experimento")
        print("3. Eliminar Experimentos")
        print("4. Analisis de Resultados")
        print("5. Comparar Experimentos")
        print("6. Gestion de Informe")
        print("7. Salir")
        opcion = input("seleccione una opcion: ")
        
        if opcion == "1":
            gestionarExperimento(listaExperimentos)
        elif opcion == "2":
            VisualizarExperimento (listaExperimentos)
        elif opcion == "3":
            print("saliendo del programa....")
        elif opcion == "4":
            print("saliendo del programa....")
        elif opcion == "5":
            print("saliendo del programa....")
            break
        else:
            print("opcion invalida")
            

if __name__ == "__main__":
    menu()        
        