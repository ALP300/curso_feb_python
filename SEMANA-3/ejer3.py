persona={"nombre":"Juan","edad":25,"ciudad":"Madrid", "profesion":"Ingeniero"}
print(persona)
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
print(persona["profesion"])
persona["nombre"]="Pedro"
print(persona)
persona["sexo"]="Masculino"
print(persona)
persona.pop("sexo")
print(persona)