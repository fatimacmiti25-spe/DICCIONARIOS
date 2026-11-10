palabras = ["sol", "luna", "sol", "estrella", "sol"]

frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)