from data_reader import leer_datos , filtrar_calcular_media

def main():
    ruta_archivo = 'C:/Users/Usuario/Desktop/examen_evaluacion/Data/datos_examen.csv'
    datos = leer_datos(ruta_archivo)

    media_por_alumno = filtrar_calcular_media(datos, 'Examen_Noelia')
 
    print("Media de la columna Value para cada alumno:")
    print(media_por_alumno)

if __name__ == "_main_":
    main()