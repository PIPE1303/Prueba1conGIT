Bot= {
        "Hola": "Hola, ¿Cómo estás hoy?",
        "Cuéntame un chiste": "¿Qué hacían dos pollitos en un asadero? --- viendo una película de terror",
        "Cuéntame otro chiste": "Qué hace un perro con un taladro --- Taladrando",
        "Chao": "Espero verte mañana"
    }
mensaje=""

while (mensaje != "Chao"):
    mensaje= input("Tú: ")
    print(Bot[mensaje])
