import statistics

def liste_nombres(nombres: list):
    '''
    Entrée : une liste de nombres
    Sortie : /

    Effectue plusieurs opérations sur une liste de nombres et affiche les résultats
    '''

    # maximum
    print(max(nombres))
    
    # minimum
    print(min(nombres))

    # moyenne
    print(statistics.mean(nombres))