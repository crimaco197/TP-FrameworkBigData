#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import csv
import re

# Leer entrada desde stdin usando csv.reader
reader = csv.reader(sys.stdin, delimiter="\t")

# Ignorar la primera línea (encabezados)
next(reader, None)

# Iterar sobre las líneas del archivo
for line in reader:
    if len(line) < 5:  # Asegurarse de que la línea tenga suficientes columnas
        continue
    
    body = line[4]  # Columna del cuerpo del post
    node_id = line[0]  # Columna node_id (identificador)

    # Eliminar etiquetas HTML del texto
    # clean_body = re.sub(r"<[^>]+>", "", body)
    
    # Extraer palabras usando regex, separadas por caracteres de puntuación o espacios
    words = re.findall(r"[\w']+", body)  # Busca palabras alfanuméricas y apóstrofes
    
    # Imprimir cada palabra con el node_id
    for word in words:
        print("{0}\t{1}".format(word.lower(), node_id))
