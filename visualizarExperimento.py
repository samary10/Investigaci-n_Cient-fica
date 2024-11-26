#funcion para consultar experimento
def VisualizarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("\n**no hay experimentos registradas**\n")
        return
    
    print(f"\nLISTA DE EXPERIMENTOS")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print("_______________________________________")
        print(f"\nExperimento {i}")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha Realizacion: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Tipo Experimento: {experimento.tipoExperimento}")
        print(f"Resultados: {experimento.resultados}\n")