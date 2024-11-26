def compararExperimentos(listaExperimentos):
    if len(listaExperimentos) < 2:
        print("**Debe haber al menos dos experimentos para comparar.**")
        return

    print("Seleccione los experimentos que desea comparar:")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"{i}. {experimento.nombre}")
    
    try:
        indices = list(map(int, input("Ingrese los números de los experimentos separados por comas: ").split(',')))
        seleccionados = [listaExperimentos[i - 1] for i in indices]
    except (IndexError, ValueError):
        print("**Selección inválida. Intente nuevamente.**")
        return

    # Preparar datos para la comparación
    resumen = []
    for experimento in seleccionados:
        valores_totales = []
        for valores in experimento.resultados.values():
            try:
                valores = list(map(float, valores))  # Convertir los valores a float
                valores_totales.extend(valores)
            except ValueError:
                print(f"**El experimento '{experimento.nombre}' contiene valores no numéricos.**")
                return

        if valores_totales:
            resumen.append({
                "nombre": experimento.nombre,
                "promedio": sum(valores_totales) / len(valores_totales),
                "maximo": max(valores_totales),
                "minimo": min(valores_totales)
            })

    # Identificar los mejores y peores experimentos
    if resumen:
        mejor = max(resumen, key=lambda x: x["promedio"])
        peor = min(resumen, key=lambda x: x["promedio"])
        
        print("\nResultados de la comparación:")
        for r in resumen:
            print(f"Experimento: {r['nombre']}, Promedio: {r['promedio']:.2f}, Máximo: {r['maximo']}, Mínimo: {r['minimo']}")
        
        print(f"\nEl experimento con el mejor rendimiento es '{mejor['nombre']}' (Promedio: {mejor['promedio']:.2f}).")
        print(f"El experimento con el peor rendimiento es '{peor['nombre']}' (Promedio: {peor['promedio']:.2f}).")
    else:
        print("**No se pudieron calcular resultados válidos.**")