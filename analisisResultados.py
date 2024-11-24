import statistics

def analisisResultados(listaExperimentos):
    if not listaExperimentos:
        print("**No hay experimentos registrados.**")
        return

    print("\nANÁLISIS DE RESULTADOS:")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}: {experimento.nombre}")
        print(f"Tipo: {experimento.tipoExperimento}")
        print(f"Fecha: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}")
        print("Resultados por variable:")

        for variable, valores in experimento.resultados.items():
            try:
                # Convierte los valores a flotantes y calcula estadísticas
                valores = list(map(float, valores))
                promedio = statistics.mean(valores)
                valor_maximo = max(valores)
                valor_minimo = min(valores)

                print(f"  Variable: {variable}")
                print(f"    - Promedio: {promedio:.2f}")
                print(f"    - Máximo: {valor_maximo}")
                print(f"    - Mínimo: {valor_minimo}")
            except ValueError:
                print(f"**Los valores de la variable '{variable}' no son válidos para el análisis numérico.**")
