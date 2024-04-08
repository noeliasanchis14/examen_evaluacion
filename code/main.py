from data_reader import leer_datos, filtrar_calcular_media

def prueba():
    """
    Esta función te leerá los datos y calculará la media por alumno
    """
    print(leer_datos(df))
    print(filtrar_calcular_media(df, 'Examen_Noelia'))

if __name__=="__main__":
    prueba()