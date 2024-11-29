import statistics
def generarInforme(listaExperimentos):
     if not listaExperimentos:
        print("**Debe haber al menos un experimento.**")
        return
     print("Seleccione los experimentos de los cuales requiere el informe:")
     for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"{i}. {experimento.nombre}")

     try:
        indices = list(map(int, input("Ingrese los números de los experimentos separados por comas: ").split(',')))
        seleccionados = [listaExperimentos[i - 1] for i in indices]
     except (IndexError, ValueError):
         print("**Selección inválida. Intente nuevamente.**")
         return
   
     with open("informe_final.txt", "w") as archivo:
        archivo.write(f"INFORME FINAL DE EXPERIMENTOS\n")
        for experimento in seleccionados:  
            archivo.write(f"\nExperimento {i}: {experimento.nombre}\n")
            archivo.write(f"Tipo: {experimento.tipoExperimento}\n")
            archivo.write(f"Fecha: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Resultados: {experimento.resultados}\n")

            archivo.write(f"\n ANALISIS DE RESULTADOS \n")
            archivo.write("\n Resultados por variable:")
            for variable, valores in experimento.resultados.items():
                valores = list(map(float, valores))
                promedio = statistics.mean(valores)
                valor_maximo = max(valores)
                valor_minimo = min(valores)
                
                archivo.write(f"  Variable: {variable}\n")
                archivo.write(f"    - Promedio: {promedio:.2f}\n")
                archivo.write(f"    - Máximo: {valor_maximo}\n")
                archivo.write(f"    - Mínimo: {valor_minimo}\n")

     print("Informe generado como 'informe_final.txt' ")