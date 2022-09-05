#
# Reto #33
# CICLO SEXAGENARIO CHINO
# Fecha publicación enunciado: 15/08/22
# Fecha publicación resolución: 22/08/22
# Dificultad: MEDIA
#
# Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
# en el ciclo sexagenario del zodíaco chino.
# - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
#   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
#   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
# - Cada elemento se repite dos años seguidos.
# - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
#
# Información adicional:
# - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Tienes toda la información sobre los retos semanales en https://retosdeprogramacion.com/semanales2022.
#
#

elementos = ["madera", "fuego", "tierra", "metal", "agua"]
animales = ["rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]
lista_combinada = list()
ano_a_validar = 0

def calcular_ano_ciclo_sexagenario(ano):
    if validar_ano_ingresado(ano) == True:
        crear_lista_combinada()
        if ano > 4:
            ano -= 3
            ano = ano - (60 * (ano // 60))
        elif ano <= 3:
            ano = abs(ano) + 2
            ano = 60 - (ano - (60 * (ano // 60)))
        print("El año {} corresponde a: {}".format(ano_a_validar, lista_combinada[ano - 1]))

def validar_ano_ingresado(ano):
    validacion = False
    while not validacion:
        if type(ano) is not int:
            print("El año ingresado no es un número entero.\nIntente de nuevo.")
            break
        elif type(ano) is int:
            validacion = True
    return validacion

def crear_lista_combinada():
    global lista_combinada
    indice_animal = 0
    indice_elemento = 0
    validacion_elemento = 0
    while len(lista_combinada) <= 59:
        lista_combinada.append(elementos[indice_elemento] + " " + animales[indice_animal])
        if indice_animal < 11:
            indice_animal += 1
        else:
            indice_animal = 0
        if validacion_elemento == 0:
            validacion_elemento += 1
        elif validacion_elemento == 1:
            validacion_elemento = 0
            if indice_elemento < 4:
                indice_elemento += 1
            else:
                indice_elemento = 0

ano_a_validar = "-246"
calcular_ano_ciclo_sexagenario(ano_a_validar)