#Libreria para descargar videos de youtube

from youtube_transcript_api import YouTubeTranscriptApi as yta
import re

#Video ejemplo de youtube
#https://www.youtube.com/watch?v=i6TyRf8d7hM

vid_id = 'i6TyRf8d7hM'

#Extraer texto
data = yta.get_transcript(vid_id, languages=['en']) #El video aparce en inglés
transcript = ''
for value in data:
    for key, val in value.items():
        if key == 'text':
            transcript += val

l = transcript.splitlines()
final_tra = " ".join(l)

#Guardar en un archivo de texto
file = open("VideoToText.txt", 'w')
file.write(final_tra)
file.close()
