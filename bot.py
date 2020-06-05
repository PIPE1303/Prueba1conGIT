from funcMiBanco import consultarvalor
Bot= {
        "Hola": "Hola, ¿Cómo estás hoy?",
        "Cuéntame un chiste": "¿Qué hacían dos pollitos en un asadero? --- viendo una película de terror",
        "Cuéntame otro chiste": "Qué hace un perro con un taladro --- Taladrando",
        "Chao": "Espero verte mañana",
        "Consultar deuda": "Ok, ingresa los valores"
    }
mensaje=""

while (mensaje != "Chao"):
    try:
        mensaje= input("Tú: ")
        print(Bot[mensaje])

        if (mensaje=="Consultar deuda"):
            consultarvalor()
    except:
        print("No entiendo tu pregunta, repítemela por favor")
    
