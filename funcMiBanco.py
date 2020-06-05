def consultarvalor():
    estrato=int(input("Ingrese el estrato de la persona: "))
    valor_deuda=float(input("Ingrese el valor de la deuda: "))

    if (estrato<5):
        interes=5
    elif(estrato<=7):
        interes=5.5
    else:
        interes=6

    porcentaje_calculado=valor_deuda*(1+interes/100)

    print("El valor de la deuda es:", valor_deuda)
    print("El estrato del deudor es:", estrato)
    print("El interés del deudor es:", interes,"%")
    print("Resultado total en porcentaje: ", porcentaje_calculado)