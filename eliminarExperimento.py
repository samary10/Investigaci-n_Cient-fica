def eliminarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados para eliminar.")
        return
    
    print("Lista de experimentos:")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"{i}. {experimento.nombre} (Fecha: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}, Tipo: {experimento.tipoExperimento})")
    
    try:
        opcion = int(input("Ingrese el número del experimento que desea eliminar: "))
        if opcion < 1 or opcion > len(listaExperimentos):
            print("**Número de experimento inválido.**")
            return
        
        experimento_seleccionado = listaExperimentos[opcion - 1]
        confirmacion = input(f"¿Está seguro de que desea eliminar el experimento '{experimento_seleccionado.nombre}'? (s/n): ").lower()
        if confirmacion == "s":
            listaExperimentos.pop(opcion - 1)
            print(f"**El experimento '{experimento_seleccionado.nombre}' ha sido eliminado.**")
        else:
            print("**Operación cancelada.**")
    except ValueError:
        print("**Debe ingresar un número válido.**")