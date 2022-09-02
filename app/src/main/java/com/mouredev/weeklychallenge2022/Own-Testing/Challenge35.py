#
# Reto #35
# BATALLA POKÉMON
# Fecha publicación enunciado: 29/08/22
# Fecha publicación resolución: 06/09/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
# - La fórmula será la siguiente: daño = 50 # (ataque / defensa) # efectividad
# - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
# - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
# - El programa recibe los siguientes parámetros:
#  - Tipo del Pokémon atacante.
#  - Tipo del Pokémon defensor.
#  - Ataque: Entre 1 y 100.
#  - Defensa: Entre 1 y 100.
#
# Información adicional:
# - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
#   para preguntas, dudas o prestar ayuda a la comunidad.
# - Tienes toda la información sobre los retos semanales en
#   https://retosdeprogramacion.com/semanales2022.
#
#

#
#    Tabla de referencias de las efectividades entre tipos (Perspectiva/Orientación: Atacante -> Defensor)
#
#           X2                      X1                          X0.5
#    Agua    Fuego           Fuego       Eléctrico       Agua        Agua
#    Fuego   Planta          Planta      Eléctrico       Agua        Planta
#    Planta  Agua            Eléctrico   Fuego           Agua        Eléctrico
#    Eléctrico Agua                                      Fuego       Agua
#                                                        Fuego       Fuego
#                                                        Planta      Fuego
#                                                        Planta      Planta
#                                                        Eléctrico   Planta
#                                                        Eléctrico   Eléctrico
#

dano = 0.0
efectividad_final = 0.0
nombre_pokemon_1 = ""
nombre_pokemon_2 = ""
tipo_pokemon_1 = ""
tipo_pokemon_2 = ""
ataque_pokemon_1 = 0
ataque_pokemon_2 = 0
defensa_pokemon_1 = 0
defensa_pokemon_2 = 0
salud_pokemon_1 = 0
salud_pokemon_2 = 0

def calcular_efectividad(tipo_pokemon_1, tipo_pokemon_2):
    if tipo_pokemon_1 == "" or type(tipo_pokemon_1) is not str:
        print("El tipo definido para el primer pokémon es vacío o no es valido.")
        return
    else:
        tipo_pokemon_1 = tipo_pokemon_1.title()
    if tipo_pokemon_2 == "" or type(tipo_pokemon_2) is not str:
        print("El tipo definido para el segundo pokémon es vacío o no es valido.")
        return
    else:
        tipo_pokemon_2 = tipo_pokemon_2.title()
    if (tipo_pokemon_1 == "Fuego" and tipo_pokemon_2 == "Eléctrico") or (tipo_pokemon_1 == "Planta" and tipo_pokemon_2 == "Eléctrico") or (tipo_pokemon_1 == "Eléctrico" and tipo_pokemon_2 == "Fuego"):
        efectividad = 1
    elif (tipo_pokemon_1 == "Agua" and tipo_pokemon_2 == "Fuego") or (tipo_pokemon_1 == "Fuego" and tipo_pokemon_2 == "Planta") or (tipo_pokemon_1 == "Planta" and tipo_pokemon_2 == "Agua") or (tipo_pokemon_1 == "Eléctrico" and tipo_pokemon_2 == "Agua"):
        efectividad = 2
    elif (tipo_pokemon_1 == "Agua" and tipo_pokemon_2 == "Agua") or (tipo_pokemon_1 == "Agua" and tipo_pokemon_2 == "Planta") or (tipo_pokemon_1 == "Agua" and tipo_pokemon_2 == "Eléctrico") or (tipo_pokemon_1 == "Fuego" and tipo_pokemon_2 == "Agua") or (tipo_pokemon_1 == "Fuego" and tipo_pokemon_2 == "Fuego") or (tipo_pokemon_1 == "Planta" and tipo_pokemon_2 == "Fuego") or (tipo_pokemon_1 == "Planta" and tipo_pokemon_2 == "Planta") or (tipo_pokemon_1 == "Eléctrico" and tipo_pokemon_2 == "Planta") or (tipo_pokemon_1 == "Eléctrico" and tipo_pokemon_2 == "Eléctrico"):
        efectividad = 0.5
    return efectividad

def validar_entradas():
    global nombre_pokemon_1
    global nombre_pokemon_2
    global tipo_pokemon_1
    global tipo_pokemon_2
    global ataque_pokemon_1
    global ataque_pokemon_2
    global defensa_pokemon_1
    global defensa_pokemon_2
    global salud_pokemon_1
    global salud_pokemon_2
    validacion = 0
    while validacion <= 10:
        if nombre_pokemon_1 == "" and type(nombre_pokemon_1) is not str:
            print("El nombre del primer pokémon es vacío o no corresponde a un valor de texto.\nIntente de nuevo.")
            break
        elif nombre_pokemon_1 != "" and type(nombre_pokemon_1) is str:
            validacion += 1
        if nombre_pokemon_2 == "" and type(nombre_pokemon_2) is not str:
            print("El nombre del segundo pokémon es vacío o no corresponde a un valor de texto.\nIntente de nuevo.")
            break
        elif nombre_pokemon_2 != "" and type(nombre_pokemon_2) is str:
            validacion += 1
        if tipo_pokemon_1 == "" and type(tipo_pokemon_1) is not str:
            print("El tipo del primer pokémon es vacío o no corresponde a un valor de texto.\nIntente de nuevo.")
            break
        elif tipo_pokemon_1 != "" and type(tipo_pokemon_1) is str:
            validacion += 1
        if tipo_pokemon_2 == "" and type(tipo_pokemon_2) is not str:
            print("El tipo del segundo pokémon es vacío o no corresponde a un valor de texto.\nIntente de nuevo.")
            break
        elif tipo_pokemon_2 != "" and type(tipo_pokemon_2) is str:
            validacion += 1
        if type(ataque_pokemon_1) is int:
            if ataque_pokemon_1 > 0 and ataque_pokemon_1 < 100:
                validacion += 1
            else:
                print("El valor del ataque ingresado para el primer pokémon es menor que 1 o mayor que 100.\nIntente de nuevo.")
                break
        elif type(ataque_pokemon_1) is not int:
            print("El valor del ataque del primer pokémon no corresponde a un valor numérico entre 1 y 100.")
        if type(ataque_pokemon_2) is int:
            if ataque_pokemon_2 > 0 and ataque_pokemon_2 < 100:
                validacion += 1
            else:
                print("El valor del ataque ingresado para el segundo pokémon es menor que 1 o mayor que 100.\nIntente de nuevo.")
                break
        elif type(ataque_pokemon_2) is not int:
            print("El valor del ataque del segundo pokémon no corresponde a un valor numérico entre 1 y 100.")
        if type(defensa_pokemon_1) is int:
            if defensa_pokemon_1 > 0 and defensa_pokemon_1 < 100:
                validacion += 1
            else:
                print("El valor de la defensa ingresado para el primer pokémon es menor que 1 o mayor que 100.\nIntente de nuevo.")
                break
        elif type(defensa_pokemon_1) is not int:
            print("El valor de la defensa del primer pokémon no corresponde a un valor numérico entre 1 y 100.")        
        if type(defensa_pokemon_2) is int:
            if defensa_pokemon_2 > 0 and defensa_pokemon_2 < 100:
                validacion += 1
            else:
                print("El valor de la defensa ingresado para el segundo pokémon es menor que 1 o mayor que 100.\nIntente de nuevo.")
                break
        elif type(defensa_pokemon_2) is not int:
            print("El valor de la defensa del segundo pokémon no corresponde a un valor numérico entre 1 y 100.")
        if type(salud_pokemon_1) is int:
            if salud_pokemon_1 > 0 and salud_pokemon_1 < 100:
                validacion += 1
            else:
                print("El valor de la salud ingresado para el primer pokémon es menor que 1 o mayor que 100.\nIntente de nuevo.")
                break
        elif type(salud_pokemon_1) is not int:
            print("El valor de la salud del primer pokémon no corresponde a un valor numérico entre 1 y 100.")        
        if type(salud_pokemon_2) is int:
            if salud_pokemon_2 > 0 and salud_pokemon_2 < 100:
                validacion += 1
            else:
                print("El valor de la salud ingresado para el segundo pokémon es menor que 1 o mayor que 100.\nIntente de nuevo.")
                break
        elif type(salud_pokemon_2) is not int:
            print("El valor de la salud del segundo pokémon no corresponde a un valor numérico entre 1 y 100.")

def dano_ataque_pokemon_1():
    global nombre_pokemon_1
    global nombre_pokemon_2
    global dano
    global efectividad_final
    global ataque_pokemon_1
    global defensa_pokemon_2
    global salud_pokemon_2
    efectividad_final = calcular_efectividad(tipo_pokemon_1, tipo_pokemon_2)
    print("La efectividad del tipo {} contra el tipo {} es: {}".format(tipo_pokemon_1, tipo_pokemon_2, efectividad_final))
    dano = 50 * (ataque_pokemon_1/defensa_pokemon_2) * efectividad_final
    salud_pokemon_2 -= dano
    print("El daño hecho por {} a {} es: {:.0f}".format(nombre_pokemon_1, nombre_pokemon_2, dano))
    if salud_pokemon_2 <= 0:
        print("La salud restante de {} es de: {:.0f}\n".format(nombre_pokemon_2, 0))
    else:
        print("La salud restante de {} es de: {:.0f}\n".format(nombre_pokemon_2, salud_pokemon_2))

def dano_ataque_pokemon_2():
    global nombre_pokemon_1
    global nombre_pokemon_2
    global dano
    global efectividad_final
    global ataque_pokemon_2
    global defensa_pokemon_1
    global salud_pokemon_1
    efectividad_final = calcular_efectividad(tipo_pokemon_2, tipo_pokemon_1)
    print("La efectividad del tipo {} contra el tipo {} es: {}".format(tipo_pokemon_2, tipo_pokemon_1, efectividad_final))
    dano = 50 * (ataque_pokemon_2/defensa_pokemon_1) * efectividad_final
    salud_pokemon_1 -= dano
    print("El daño hecho por {} a {} es: {:.0f}".format(nombre_pokemon_2, nombre_pokemon_1, dano))
    if salud_pokemon_1 <= 0:
        print("La salud restante de {} es de: {:.0f}\n".format(nombre_pokemon_1, 0))
    else:
        print("La salud restante de {} es de: {:.0f}\n".format(nombre_pokemon_1, salud_pokemon_1))

def carga_valores_pokemon_1(nombre_1, tipo_1, salud_1, ataque_1, defensa_1):
    global nombre_pokemon_1
    global tipo_pokemon_1
    global salud_pokemon_1
    global ataque_pokemon_1
    global defensa_pokemon_1
    nombre_pokemon_1 = nombre_1
    tipo_pokemon_1 = tipo_1
    salud_pokemon_1 = salud_1
    ataque_pokemon_1 = ataque_1
    defensa_pokemon_1 = defensa_1

def carga_valores_pokemon_2(nombre_2, tipo_2, salud_2, ataque_2, defensa_2):
    global nombre_pokemon_2
    global tipo_pokemon_2
    global salud_pokemon_2
    global ataque_pokemon_2
    global defensa_pokemon_2 
    nombre_pokemon_2 = nombre_2
    tipo_pokemon_2 = tipo_2
    salud_pokemon_2 = salud_2
    ataque_pokemon_2 = ataque_2
    defensa_pokemon_2 = defensa_2

def inicia_batalla():
    global nombre_pokemon_1
    global tipo_pokemon_1
    global salud_pokemon_1
    global ataque_pokemon_1
    global defensa_pokemon_1
    global nombre_pokemon_2
    global tipo_pokemon_2
    global salud_pokemon_2
    global ataque_pokemon_2
    global defensa_pokemon_2 
    print("¿Deseas ingresar tus propios valores para la batalla?\n¿O usaras los valores determinados para prueba?\n1-Ingresar valores.\n2-Usar valores de prueba.")
    decision = input()
    print("¡INICIA LA BATALLA POKÉMON!")
    if decision == "1":
        nombre_pokemon_1 = input("Ingresa el nombre del primer pokémon: ")
        tipo_pokemon_1 = input("Ingresa el tipo de {} (Agua, Fuego, Planta y Eléctrico): ".format(nombre_pokemon_1))
        salud_pokemon_1 = int(input("Ingresa la salud de {}: ".format(nombre_pokemon_1)))
        ataque_pokemon_1 = int(input("Ingresa el ataque de {} (un valor entre 1 y 100): ".format(nombre_pokemon_1)))
        defensa_pokemon_1 = int(input("Ingresa la defensa de {} (un valor entre 1 y 100): ".format(nombre_pokemon_1)))
        nombre_pokemon_2 = input("Ingresa el nombre del segundo pokémon: ")
        tipo_pokemon_2 = input("Ingresa el tipo de {}: ".format(nombre_pokemon_2))
        salud_pokemon_2 = int(input("Ingresa la salud de {}: ".format(nombre_pokemon_2)))
        ataque_pokemon_2 = int(input("Ingresa el ataque de {} (un valor entre 1 y 100): ".format(nombre_pokemon_2)))
        defensa_pokemon_2 = int(input("Ingresa la defensa de {} (un valor entre 1 y 100): ".format(nombre_pokemon_2)))
        validar_entradas()
        while salud_pokemon_1 > 0 or salud_pokemon_2 > 0:
            dano_ataque_pokemon_1()
            if salud_pokemon_2 == 0 or salud_pokemon_2 < 0:
                print("El pokémon {} ha sido vencido.".format(nombre_pokemon_2))
                print("El pokémon ganador es {}.".format(nombre_pokemon_1))
                break
            dano_ataque_pokemon_2()
            if salud_pokemon_1 == 0 or salud_pokemon_1 < 0:
                print("El pokémon {} ha sido vencido.".format(nombre_pokemon_1))
                print("El pokémon ganador es {}.".format(nombre_pokemon_2))
                break
    elif decision == "2":
        carga_valores_pokemon_1("Pikachu", "Eléctrico", 100, 66, 48)
        carga_valores_pokemon_2("Magmar", "Fuego", 132, 73, 59)
        while salud_pokemon_1 > 0 or salud_pokemon_2 > 0:
            dano_ataque_pokemon_1()
            if salud_pokemon_2 == 0 or salud_pokemon_2 < 0:
                print("El pokémon {} ha sido vencido.".format(nombre_pokemon_2))
                print("El pokémon ganador es {}.".format(nombre_pokemon_1))
                break
            dano_ataque_pokemon_2()
            if salud_pokemon_1 == 0 or salud_pokemon_1 < 0:
                print("El pokémon {} ha sido vencido.".format(nombre_pokemon_1))
                print("El pokémon ganador es {}.".format(nombre_pokemon_2))
                break
    elif decision == "3":
        carga_valores_pokemon_1("Torterra", "Planta", 253, 108, 96)
        carga_valores_pokemon_2("Blaziken", "Fuego", 241, 91, 88)
        while salud_pokemon_1 > 0 or salud_pokemon_2 > 0:
            dano_ataque_pokemon_1()
            if salud_pokemon_2 == 0 or salud_pokemon_2 < 0:
                print("El pokémon {} ha sido vencido.".format(nombre_pokemon_2))
                print("El pokémon ganador es {}.".format(nombre_pokemon_1))
                break
            dano_ataque_pokemon_2()
            if salud_pokemon_1 == 0 or salud_pokemon_1 < 0:
                print("El pokémon {} ha sido vencido.".format(nombre_pokemon_1))
                print("El pokémon ganador es {}.".format(nombre_pokemon_2))
                break
    elif decision != "1" and decision != "2" and decision != 3:
        print("El valor ingresado no es una decisión válida.")

inicia_batalla()