import statistics

def liste_nombres(nombres: list):
    '''
    Entrée : une liste de nombres
    Sortie : /

    Effectue plusieurs opérations sur une liste de nombres et affiche les résultats
    '''

    # maximum
    maximum = max(nombres)
    
    # minimum
    minimum = min(nombres)

    # moyenne
    moyenne = statistics.mean(nombres)

    return maximum, minimum, moyenne


liste_nombres([5,10,8,3])