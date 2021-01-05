



print("Haz tu pregunta. Para acabar escribe SALIR")

query = input()

while query != "SALIR":


    Respuesta = ""

    if  query.find("hola") != -1:
        Respuesta = "¿Que tal?"

    print (Respuesta)

    print("Haz tu pregunta. Para acabar escribe SALIR")

    query = input()