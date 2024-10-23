# Video_a_Texto
Este script de Python descarga la transcripción (subtítulos) de un video de YouTube y la guarda como un archivo de texto. Se puede utilizar para extraer y almacenar transcripciones de videos de YouTube que tienen subtítulos disponibles en inglés o en cualquier otro idioma compatible.

## Características
  * Extraer transcripción: Descarga la transcripción de un video de YouTube en el idioma especificado.
  * Guardar transcripción: Almacena la transcripción extraída en un archivo de texto simple para referencia futura.

## Requisitos
Asegúrate de tener Python instalado y luego instala el paquete necesario usando pip:

```bash
pip install youtube-transcript-api
```

## Cómo Usar
1. Establecer el ID del Video de YouTube: Reemplaza la variable `vid_id` en el script con el ID del video de YouTube del que deseas descargar la transcripción. Por ejemplo, para la URL del video `https://www.youtube.com/watch?v=i6TyRf8d7hM`, el ID del video es `i6TyRf8d7hM`.

2. Ejecutar el Script: El script realizará las siguientes acciones.
   * Descargar la transcripción para el video en el idioma especificado (`en` para inglés en este ejemplo).
   * Guardar la transcripción en un archivo de texto llamado `VideoToText.txt`.
     
3. Acceder a la Transcripción: Después de ejecutar el script, revisa el directorio donde se encuentra el script para el archivo VideoToText.txt, que contiene la transcripción del video.

## Ejemplo
```bash
# ID del video de YouTube
vid_id = 'i6TyRf8d7hM'

# Extraer la transcripción
data = yta.get_transcript(vid_id, languages=['en'])  # Cambia 'en' por otro idioma si es necesario

# Procesar y guardar la transcripción en un archivo de texto
file = open("VideoToText.txt", 'w')
file.write(transcript)
file.close()
```

## Salida
La transcripción se guardará en `VideoToText.txt`, y podrás verla o procesarla según sea necesario.

## Notas
El video debe tener subtítulos disponibles en el idioma especificado.
El script está configurado actualmente para descargar transcripciones en inglés. Puedes modificar el parámetro `languages` para cambiar el idioma de la transcripción, siempre que el video soporte ese idioma.
