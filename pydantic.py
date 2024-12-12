# Implementacion de la libreria pydantic

from pydantic import BaseModel

class usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int
    correo: str
    direccion: str
    telelfono: str
    pasatiempos: list
    sexo: str
    pais: str



datos = { "nombre":"Anderson","apellido":"Manjarres","edad":33,"correo":"ammyem@hotmail.es",
         "direccion":"Calle 89a#38-66","pasatiempos":["Jugar","Comer","Dormir","Estudiar"],
         "sexo":"Masculino","pais":"Colombia","telelfono":"3124892618" }

# crear una instacia de la clase 

usuario = usuario(**datos)

print(usuario)

print(usuario.nombre)
print(usuario.apellido)
print(usuario.edad)
print(usuario.correo)
print(usuario.direccion)
print(usuario.pasatiempos)