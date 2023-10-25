def calcul_simple(elements: list)-> float:
    '''
    Entrée : elements, la liste contenant les deux nombres ainsi que le signe d'opération
    Sortie : le résultat du calcul

    Effectue un calcul simple via un opérateur entre deux nombres
    '''

    nombre_1 = (float)(elements[0])
    nombre_2 = (float)(elements[2])
    operateur = (elements[1])

    if (operateur == "+"):
        return nombre_1 + nombre_2
    elif (operateur == "-"):
        return nombre_1 - nombre_2
    elif (operateur == "*"):
        return nombre_1 * nombre_2
    elif (operateur == "/"):
        return nombre_1 / nombre_2

# ===========================================================

calcul = str(input("Veuillez entrer une opération simple (addition, soustraction, multiplication, division) : "))
calcul_list: list = calcul.split(" ")
calcul_simple(calcul_list)