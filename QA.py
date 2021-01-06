



Ingredientes = ["huevos","mantequilla","leche","harina","azucar","sal"]



print("Haz tu pregunta. Para acabar escribe SALIR")
query = input().lower()


while query != "salir":


    Respuesta = ""

    if  query.find("hola") != -1:
        Respuesta = "¿Que tal?"

    elif ((query.find("cuales") != -1) or (query.find("que")!= -1)) and (query.find("ingredientes")!= -1):
        Respuesta = "ingredientes"


    elif ((query.find("cuanta") != -1) or (query.find("cantidad")!= -1)) and (any(ingredients in query for ingredients in Ingredientes)):
        Respuesta = "cantidad"    

        if (query.find("huevos")!= -1):
            Respuesta = "cantidad"
        if (query.find("mantequilla")!= -1):
            Respuesta = "cantidad"
        if (query.find("leche")!= -1):
            Respuesta = "cantidad"
        if (query.find("harina")!= -1):
            Respuesta = "cantidad"
        if (query.find("azucar")!= -1):
            Respuesta = "cantidad"
        if (query.find("sal")!= -1):
            Respuesta = "cantidad"

    elif (((query.find("cuanto") != -1) and (query.find("tiempo"))) or (query.find("cuando")!= -1)) and (any(ingredients in query for ingredients in Ingredientes)):
        Respuesta = "tiempo"    

        if (query.find("huevos")!= -1):
            Respuesta = "tiempo" 
        if (query.find("mantequilla")!= -1):
            Respuesta = "tiempo" 
        if (query.find("leche")!= -1):
            Respuesta = "tiempo" 
        if (query.find("harina")!= -1):
            Respuesta = "tiempo" 
        if (query.find("azucar")!= -1):
            Respuesta = "tiempo" 
        if (query.find("sal")!= -1):
            Respuesta = "tiempo" 

    elif ((query.find("quien") != -1) or (query.find("autor")!= -1)) and (query.find("receta")!= -1):
        Respuesta = "autor"

    elif ((query.find("cuales") != -1) or (query.find("que")!= -1)) and (query.find("pasos")!= -1):
        Respuesta = "preparacion"
            
    elif (query.find("que") != -1) and ((query.find("hacer")) or (query.find("hace")!= -1)) and (any(ingredients in query for ingredients in Ingredientes)):
        Respuesta = "preparacion"    

        if (query.find("huevos")!= -1):
            Respuesta = "preparacion" 
        if (query.find("mantequilla")!= -1):
            Respuesta = "preparacion" 
        if (query.find("leche")!= -1):
            Respuesta = "preparacion" 
        if (query.find("harina")!= -1):
            Respuesta = "preparacion" 
        if (query.find("azucar")!= -1):
            Respuesta = "preparacion" 
        if (query.find("sal")!= -1):
            Respuesta = "preparacion" 
            

    elif ((query.find("consejos") != -1) or (query.find("recomiendas")!= -1)):
        Respuesta = "consejos"        

    elif ((query.find("utensilios") != -1)):
        Respuesta = "utensilios"

    elif ((query.find("acompañamientos") != -1) or (query.find("añadir")!= -1)):
        Respuesta = "acompañamientos"

       

    print(Respuesta)

    print("Haz tu pregunta. Para acabar escribe SALIR")

    query = input().lower()
    


