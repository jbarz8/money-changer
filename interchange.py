menu = """
Bienvenido al conversor de monedas 💲 Ingrese las opciones:
1) Para pesos colombianos.
2.) pesos argentinos

Ingresa un Número: """

def run(valor_dolar, tipo_pesos):
    pesos = int(input("Ingresa la cantidad de pesos " + tipo_pesos + " que tienes sin puntos ni comas: "))
    dolar = pesos / valor_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Tienes $ " + dolar + " dolares en pesos " + tipo_pesos)

opciones = int(input(menu))
    

if  opciones == 1:
    run(3715, "colombianos")

elif opciones == 2:
    run(94, "argentinos")

else:
    print("Ingresa una opcion correcta")
    
    

