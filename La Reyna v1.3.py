#La hoja de calclulo va a estar en otra carpeta
#Aqui se va a desplegar el menu (todas las opciones)

orden = [] #lista que se va a comparar con la hoja de datos para ver el precio
#orden va a ser hasta después ahorita no se le va agregar nada
drinks = []
comidas = []

bebidastotal = 0 
comidastotal = 0

print("Bienvenidos a La Reyna")

# Función para ordenar las bebidas
def order_drinks():
    drinksqacorrect = ["Si", "si", "Sí", "sí", "S", "s", "Y", "y"]
    drinksqa = input("Les gustaría ordenar algo para beber? ")

    if drinksqa in drinksqacorrect:
        numdrink = int(input("¿Cuántas bebidas desea? "))
        for i in range(numdrink):
            drink = input("""¿Qué bebidas les gustaría ordenar? Por favor ordene una por una:
   Agua - $30
   Refresco - $50
   Jugo - $50
   Agua del Día - $60
   Licuado - $80
   Malteada - $90
   """)
            drinks.append(drink)
        print("Perfecto, su orden de bebidas es: ", drinks)
    else:
        drinks.append("ninguna bebida") 
        print(drinks)

# Función para ordenar comida
def order_food():
    foodqacorrect = ["Si", "si", "Sí", "sí", "S", "s"]
    foodqa = input("Les gustaría ordenar algo para comer? ")

    if foodqa in foodqacorrect:
        numcomida = int(input("¿Cuántas comidas desea? "))
        for i in range(numcomida):
            food = input("""¿Qué comida les gustaría ordenar?
   Torta de Milanesa - $90
   Torta de Milanesa con queso - $100
   Torta de Pierna - $90
   Torta de Pierna con queso - $100
   Torta de Chile Relleno - $90
   Torta de Jamon y Queso - $80
   Torta de Carne - $90
   """)
            comidas.append(food)
        print("Perfecto, su orden de comidas es: ", comidas)
    else:
        comidas.append("ninguna comida")
        print(comidas)
    
# Llamando las funciones
order_drinks()
order_food()

extras = []
extrasansw = ["Si", "si", "Sí", "sí", "S", "s", "Y", "y"]
extrasagu = input("¿Les gustaría añadir aguacate a su pedido? ")
if extrasagu in extrasansw:
    extras.append("con aguacate")
else: 
    extras.append("sin aguacate")
extrassals = input("¿Les gustaría añadir salsa a su pedido? ")
if extrassals in extrasansw:
    extras.append("con salsa")
else:
    extras.append("sin salsa")

# Orden final
print("Su orden es", drinks, "y", comidas, extras)