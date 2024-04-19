import pandas as pd

# lista edades
lista_edades = [19,29,19,22,23,19,30,19,19,19,20,20,20,18,22,19,34,34,21,21,22,28,29,19,20,19,25,28,21,22]



def analisis_estadistico(lista_edades):

    # convertir la lista en una serie
    series_edades = pd.Series(lista_edades)
    # Calcular la frecuencia absoluta ( fi )
    fi = series_edades.value_counts()
    # Ordenar el diccionario por las claves (edades) de menor a mayor
    fi = dict(sorted(fi.items()))
    # Crear DataFrame 
    data_frame = pd.DataFrame(fi.items(), columns=['Edad', 'fi'])


    # Calcular la frecuencia acumulada (Fi)
    data_frame["Fi"] = data_frame["fi"].cumsum()

    # Calcular la frecuencia relativa (ri)
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()

    # Calcular la frecuencia relativa acumulada (Ri)
    data_frame["Ri"] = data_frame["ri"].cumsum()

    # Calcular la probabilidad (pi%)
    data_frame['pi%'] = data_frame["ri"] * 100

    # Calcular la probabilidad acumulada (Pi%)
    data_frame["Pi%"] = data_frame["Ri"] * 100

    # Retornar el DataFrame resultante
    return data_frame


resultado_analisis = analisis_estadistico(lista_edades)
print(resultado_analisis.to_string(index=False))



