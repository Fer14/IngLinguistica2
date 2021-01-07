



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

    elif ((query.find("cuando")!= -1) or (query.find("fecha")!= -1)) and (query.find("diogenes")!=-1):
    	if ((query.find("nacio")!= -1) or (query.find("nacimiento")!= -1)):
    		Respuesta ="412 a.C"
    	if ((query.find("murio")!= -1) or (query.find("defuncion")!= -1)):
    		Respuesta ="412 a.C"


    elif ((query.find("donde")!= -1) or (query.find("lugar")!= -1)) and (query.find("diogenes")!=-1):
    	if ((query.find("nacio")!= -1) or (query.find("nacimiento")!= -1)):
    		Respuesta ="Synope"
    	if ((query.find("murio")!= -1) or (query.find("defuncion")!= -1)):
    		Respuesta ="Corinto"
    	if ((query.find("vivio")!= -1) or (query.find("vida")!= -1)):
    		Respuesta ="Las calles de Atenas"

    elif ((query.find("cuales")!= -1) or (query.find("como")!= -1)) and ((query.find("nombres")!= -1) or (query.find("llama")!= -1)):
    	if (query.find("diogenes")!= -1):
    		Respuesta ="“Diógenes de Synope o Diógenes el Cinico”"
    	if (query.find("padre"):
    		Respuesta = "Hicesias"
    	if (query.find("maestro"):
    		Respuesta = "Antístenes el más antiguo pupilo de Sócrates"

    elif ((query.find("trabajo") != -1) or (query.find("acupacion")!= -1)) and (query.find("padre") != -1):
        Respuesta = "Banquero"

    elif  (query.find("cual") != -1) and (query.find("filosofia de vida")!= -1)
    	Respuesta = "renunciar por todas partes lo convencional y oponer a ello su naturaleza"

    elif ((query.find("tenido") != -1) or (query.find("viviendo")!= -1)) and (query.find("qué") != -1):
        Respuesta = "un manto, un zurrón, un báculo y un cuenco"

    elif ((query.find("cual")!= -1) or (query.find("que")!= -1)) and ((query.find("mision")!= -1) or (query.find("hecho")!= -1)) and (query.find("Atenas") != -1):
        Respuesta = "de metafóricamente falsificar/desfigurar la “moneda” de las costumbres"

    elif ((query.find("definicion") != -1) and (query.find("costumbre")!= -1)):
        Respuesta = "la falsa moneda de la moralidad"

    elif (query.find("exilio")!= -1):
    	if ((query.find("por que")!= -1) or (query.find("razon")!= -1)): 
        	Respuesta = "desterrados por haber fabricado moneda falsa"
        if (query.find("de donde")!= -1) : 
        	Respuesta = "exiliado de su ciudad natal Synope"

    elif ((query.find("a quien") != -1) or (query.find("cual fue")!= -1)) and ((query.find("conocia") != -1) or (query.find("conocidas") != -1)):
        Respuesta = "Alejandro Magno y Platón"

    elif ((query.find("como") != -1) or (query.find("manera")!= -1)) and (query.find("murio") != -1) and (query.find("diogenes") != -1):
        Respuesta = "murió de un cólico provocado por la ingestión de un pulpo vivo o murió al caerse de un caballo o haberle mordido un tendón uno de los perros entre los que trataba de repartir un pulpo o murió por su propia voluntad, reteniendo la respiración"

    elif (query.find("cuales") != -1) and (query.find("ultimas palabres")!= -1) and (query.find("diogenes")!= -1) :
        Respuesta = "Cuando me muera, echadme a los perros. Ya estoy acostumbrado"



    print(Respuesta)

    print("Haz tu pregunta. Para acabar escribe SALIR")

    query = input().lower()
    


